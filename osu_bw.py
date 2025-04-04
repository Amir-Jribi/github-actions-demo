import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class OsubwTest(rfm.RunOnlyRegressionTest):
    descr="Reframe Osu bw test on compute Node"
    valid_systems=["my_cluster:compute_osu"]
    valid_prog_environs=["intel_osu"]
    CC='icc'
    CXX='icpc'
    FC='ifort'
    MPICC='mpiicc'
    reference={
        'my_cluster:compute_osu':{
            'bw_value':(12250,-0.03,0.03,'MB/s')
        }
    }
    @run_before('run')
    def setup_slurm(self):
        self.num_tasks=2
        self.num_tasks_per_node=1
        self.num_cpus_per_task=56
        self.time_limit = '10m30s'
        self.exclusive_access = True
        self.job.options += []
    sourcesdir='/home/amir.jribi-ext/benchmarks/osu/intel/build/libexec/osu-micro-benchmarks/mpi/pt2pt'

    #@run_before('run')
    #def setup_env_vars(self):
        #self.env_vars['CC']=self.CC
        #self.env_vars['CXX']=self.CXX
        #self.env_vars['FC']=self.FC
        #self.env_vars['MPICC']=self.MPICC

    @run_before('run')
    def execute(self):
        self.executable = './osu_bw'
        self.executable_opts = []
    #@run_before('run')
    #def set_slurm_partition(self):
       # self.job.options += ['--nodes=1']


    @sanity_function
    def validate(self):
        return sn.assert_found(r'.*', self.stdout)
    @performance_function('MB/s')
    def bw_value(self):
        return sn.extractsingle(r'4194304\s+(\d+)', self.stdout, 1, float)



