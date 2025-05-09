import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class FsCheck(rfm.RunOnlyRegressionTest):
    variant = parameter (['xfs','nfs','lustre'])
    descr = 'Filesystem mount check'
    valid_systems = ['my_cluster:compute_env']
    valid_prog_environs=["default"]
    executable='mount'
    @sanity_function
    def validate(self):
        if (self.variant=='xfs'):
            return sn.assert_found(r'/dev/sda1.*on /.*type xfs', self.stdout)
        elif(self.variant=='lustre'):
            return sn.assert_found(r'10\.44\.3\.6@o2ib2:10\.44\.3\.5@o2ib2:/lustre01.*on /srv/lustre01.*type lustre', self.stdout)
        elif(self.variant=='nfs'):
            return sn.assert_found(r'isilon:/HOME.*on /home.*type nfs', self.stdout)
