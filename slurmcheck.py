import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class SlurmCheckTest(rfm.RunOnlyRegressionTest):
    variant = parameter (['slurmctld','squeue','sacct'])
    descr="Reframe Slurm Check Test"
    valid_systems = ['my_cluster:compute_env']
    valid_prog_environs=["default"]

    @run_before('run')
    def setting_varaibles(self):
        if self.variant=="slurmctld":
            self.executable = 'scontrol ping'
            self.sanity_patterns = sn.assert_found(r'Slurmctld\(primary\) at slurm-slurm-h22a8-u17-sv is UP',self.stdout)
        elif self.variant == "squeue":
            self.executable='squeue -u amir.jribi-ext'
            self.sanity_patterns =sn.assert_found(r'NODELIST',self.stdout)
        elif self.variant == "sacct":
            self.executable='sacct'
            self.sanity_patterns=sn.assert_found(r'JobID           JobName  Partition    Account  AllocCPUS      State ExitCode',self.stdout)
