import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class ModuleSystemTest(rfm.RunOnlyRegressionTest):
    variant = parameter (['avail','load','purge'])
    descr="Reframe Module System Test"
    valid_systems=["my_cluster:compute_env"]
    valid_prog_environs=["default"]

    @run_before('run')
    def setting_varaibles(self):
        if self.variant=="avail":
            self.executable = 'echo $MODULEPATH'
            self.sanity_patterns = sn.assert_found(r'/opt/ohpc/pub/modulefiles:/srv/software/easybuild/modules/all:/srv/software/modulefiles',self.stdout)
        elif self.variant == "load":
            self.prerun_cmds=['module load GCC/13.2.0']
            self.executable='module list'
            self.sanity_patterns =sn.assert_found(r'GCC/13.2.0',self.stdout)
        elif self.variant == "purge":
            self.prerun_cmds=['module load GCC/13.2.0','module purge']
            self.executable='module list'
            self.sanity_patterns=sn.assert_found(r'No modules loaded',self.stdout)
