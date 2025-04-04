site_configuration = {
    'systems': [
        {
            'name': 'my_cluster',  # Your cluster name
            'descr': 'Cluster with Slurm scheduler',
            'modules_system': 'lmod',
            'hostnames': ['slurm-login-h23d5-u38-svn1.cloud.um6p.ma'],  # Login node hostname
            'partitions': [
                {
                    'name': 'compute_hpl',
                    'scheduler': 'slurm',
                    'launcher': 'mpirun',  # Ensures jobs run on compute nodes
                    'environs': ['intel_hpl'],
                },
                {
                    'name': 'compute_osu',
                    'scheduler': 'slurm',
                    'launcher': 'mpirun',
                    'environs': ['intel_osu'],
                },
            ]
        }
    ],
    "environments": [
     {
            'name': 'intel_hpl',  # intel environment
            'cc': 'icc',  # intel C compiler
            'cxx': 'icpc',  # intel C++ compiler
            'ftn': 'ifort',  # intel Fortran compiler
            'modules' : ['intel-compilers/2022.2.0' , 'imkl/2021.3.0-gompi-2021a' , ' impi/2021.7.0-intel-compilers-2022.2.0'],
    },
     {
            'name': 'intel_osu',  # intel environment
            'cc': 'icc',  # intel C compiler
            'cxx': 'icpc',  # intel C++ compiler
            'ftn': 'ifort',  # intel Fortran compiler
            'modules' : ['intel-compilers/2022.2.0'  ,
            ' impi/2021.7.0-intel-compilers-2022.2.0'],
    }
  ]
}

