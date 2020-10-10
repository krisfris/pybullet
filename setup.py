
from distutils.core import Extension, setup
from Cython.Distutils import build_ext

setup(
    name="bullet",
    version='0.1.0',
    packages=["bullet"],
    ext_modules=[Extension(
        "bullet.bullet",
        ["bullet/bullet.pyx"],
        libraries=[
                "BulletSoftBody",
                "BulletDynamics",
                "BulletCollision",
                "LinearMath",
                ],
        language="c++")],
    cmdclass={'build_ext': build_ext},
    )
