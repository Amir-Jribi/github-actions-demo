import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class HPLTest(rfm.RunOnlyRegressionTest):
    descr="Reframe HPL Test on compute Node"
    valid_systems=["my_cluster:compute_hpl"]
    valid_prog_environs=["intel_hpl"]
    #sourcesdir = '/home/amir.jribi-ext/use-reframe/hpl_test'
    sourcesdir = '/home/amir.jribi-ext/benchmarks/hpl/mp_linpack'
    reference={
        'my_cluster:compute_hpl':{
            'gflops_value':(2500,-0.2,0.2,'Gflops')
        }
    }
    @run_before('run')
    def setup_slurm(self):
        self.num_tasks=1
        self.num_tasks_per_node=1
        self.num_cpus_per_task=56
        self.time_limit = '10m30s'
        self.exclusive_access = True
        self.job.options += []


    
    #executable = '/home/amir.jribi-ext/benchmarks/hpl/mp_linpack/xhpl'
    executable = './xhpl'
    executable_opts = []
    #executable = './stream_c.exe'
    #@run_before('run')
    #def set_slurm_partition(self):
       # self.job.options += ['--nodes=1']


    @sanity_function
    def validate(self):
        return sn.assert_found(r'PASSED', self.stdout)

    @performance_function('Gflops')
    def gflops_value(self):
        return sn.extractsingle(r'Gflops\s+.*\nWC00C2R2\s+\d+\s+\d+\s+\d+\s+\d+\s+\d+\.\d+\s+([-+]?\d*\.?\d+(?:[eE][-+]?\d+)?)', self.stdout, 1, float)



