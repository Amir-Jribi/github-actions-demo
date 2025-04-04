import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class StreamTest(rfm.RegressionTest):
    build_system = 'SingleSource'
    @run_before('compile')
    def setup_build(self):
        self.build_system.cflags = ['-DOFFSET=0', '-DSTREAM_TYPE=double', '-Wall', '-O3', '-xCORE-AVX512', '-qopt-zmm-usage=high', '-mcmodel=medium', '-qopenmp', '-shared-intel',
                '-qopt-streaming-stores=always']
 
    descr="Reframe Stream Test on compute Node"
    valid_systems=["my_cluster:compute_stream"]    
    valid_prog_environs=["intel"]
    num_threads = 56
    affinity = 'compact'
    @run_before('run')
    def setup_slurm(self):
        self.num_tasks=1
        self.num_tasks_per_node=1
        self.num_cpus_per_task=56
        self.time_limit = '10m30s'
        self.exclusive_access = True
        self.job.options += []

    @run_before('run')
    def setup_threading(self):
        self.env_vars['OMP_NUM_THREADS']=self.num_threads
        self.env_vars['KMP_AFFINITY']=self.affinity
    sourcesdir = '/home/amir.jribi-ext/benchmarks/STREAM/'
    sourcepath = 'stream.c'


    def execute(self):
        self.executable = './stream_c.exe'
        self.executable_opts = []
    #executable = './stream_c.exe'
    #@run_before('run')
    #def set_slurm_partition(self):
       # self.job.options += ['--nodes=1']


    @sanity_function
    def validate(self):
        return sn.assert_found(r'Solution Validates', self.stdout)

    @performance_function('MB/s')
    def triad_bw(self):
        return sn.extractsingle(r'Triad:\s+(\S+)', self.stdout, 1, float)



