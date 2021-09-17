from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

setup(
    name='masking',
    ext_modules=[
        CUDAExtension(
          name='masking', 
          sources=['ampere_mask/ampere_mask.cpp','ampere_mask/ampere_mask_cuda.cu']
        )
    ],
    cmdclass={
        'build_ext': BuildExtension
    }
)