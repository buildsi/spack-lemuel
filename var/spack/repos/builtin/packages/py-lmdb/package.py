# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyLmdb(PythonPackage):
    """ Universal Python binding for the LMDB 'Lightning' Database"""

    pypi = "lmdb/lmdb-1.3.0.tar.gz"
    homepage = "https://github.com/jnwatson/py-lmdb/"

    version('1.3.0', sha256='60a11efc21aaf009d06518996360eed346f6000bfc9de05114374230879f992e')

    depends_on('python@2.7:2,3.4:', type=('build', 'run'))
    depends_on('py-setuptools', type='build')
    depends_on('lmdb')

    def setup_build_environment(self, env):
        env.set('LMDB_FORCE_SYSTEM', '1')
