OS Support by Linux Distributions and Version
==============================================

The following matrix shows which Linux distributions, containers, and images are supported with which versions of ScyllaDB.

Where *supported* in this scope means:

 .. REMOVE IN FUTURE VERSIONS - Remove information about versions from the notes below in version 5.2.

- A binary installation package is available to `download <https://www.scylladb.com/download/>`_.
- The download and install procedures are tested as part of ScyllaDB release process for each version.
- An automated install is included from :doc:`ScyllaDB Web Installer for Linux tool </getting-started/install-scylla/scylla-web-installer>` (for latest versions)

You can `build ScyllaDB from source <https://github.com/scylladb/scylladb#build-prerequisites>`_ on other x86_64 or aarch64 platforms, without any guarantees.

.. note::
   
   **Supported Architecture**

   ScyllaDB Open Source supports x86_64 for all versions and AArch64 starting from ScyllaDB 4.6 and nightly build. In particular, aarch64 support includes AWS EC2 Graviton.


ScyllaDB Open Source
----------------------

.. note:: 

    Recommended OS and ScyllaDB AMI/Image OS for ScyllaDB Open Source:

       - Ubuntu 20.04 for versions 4.6 and later.
       - CentOS 7 for versions earlier than 4.6.


+----------------------------+----------------------------------+-----------------------------+---------+-------+
| Linux Distributions        |       Ubuntu                     |    Debian                   | CentOS /| Rocky/|
|                            |                                  |                             | RHEL    | RHEL  |
+----------------------------+------+------+------+------+------+------+------+-------+-------+---------+-------+
| ScyllaDB Version / Version | 14.04| 16.04| 18.04|20.04 |22.04 | 8    | 9    |  10   |  11   | 7       |   8   |
+============================+======+======+======+======+======+======+======+=======+=======+=========+=======+
|   5.1                      | |x|  | |x|  | |v|  | |v|  | |v|  | |x|  | |x|  | |v|   | |v|   | |v|     | |v|   |
+----------------------------+------+------+------+------+------+------+------+-------+-------+---------+-------+
|   5.0                      | |x|  | |x|  | |v|  | |v|  | |v|  | |x|  | |x|  | |v|   | |v|   | |v|     | |v|   |
+----------------------------+------+------+------+------+------+------+------+-------+-------+---------+-------+
|   4.6                      | |x|  | |v|  | |v|  | |v|  | |x|  | |x|  | |v|  | |v|   | |x|   | |v|     | |v|   |
+----------------------------+------+------+------+------+------+------+------+-------+-------+---------+-------+
|   4.5                      | |x|  | |v|  | |v|  | |v|  | |x|  | |x|  | |v|  | |v|   | |x|   | |v|     | |v|   |
+----------------------------+------+------+------+------+------+------+------+-------+-------+---------+-------+
|   4.4                      | |x|  | |v|  | |v|  | |v|  | |x|  | |x|  | |v|  | |v|   | |x|   | |v|     | |v|   |
+----------------------------+------+------+------+------+------+------+------+-------+-------+---------+-------+
|   4.3                      | |x|  | |v|  | |v|  | |v|  | |x|  | |x|  | |v|  | |v|   | |x|   | |v|     | |v|   |
+----------------------------+------+------+------+------+------+------+------+-------+-------+---------+-------+
|   4.2                      | |x|  | |v|  | |v|  | |x|  | |x|  | |x|  | |v|  | |v|   | |x|   | |v|     | |v|   |
+----------------------------+------+------+------+------+------+------+------+-------+-------+---------+-------+
|   4.1                      | |x|  | |v|  | |v|  | |x|  | |x|  | |x|  | |v|  | |v|   | |x|   | |v|     | |v|   |
+----------------------------+------+------+------+------+------+------+------+-------+-------+---------+-------+
|   4.0                      | |x|  | |v|  | |v|  | |x|  | |x|  | |x|  | |v|  | |x|   | |x|   | |v|     | |x|   |
+----------------------------+------+------+------+------+------+------+------+-------+-------+---------+-------+
|   3.x                      | |x|  | |v|  | |v|  | |x|  | |x|  | |x|  | |v|  | |x|   | |x|   | |v|     | |x|   |
+----------------------------+------+------+------+------+------+------+------+-------+-------+---------+-------+
|   2.3                      | |v|  | |v|  | |v|  | |x|  | |x|  | |v|  | |v|  | |x|   | |x|   | |v|     | |x|   |
+----------------------------+------+------+------+------+------+------+------+-------+-------+---------+-------+
|   2.2                      | |v|  | |v|  | |x|  | |x|  | |x|  | |v|  | |x|  | |x|   | |x|   | |v|     | |x|   |
+----------------------------+------+------+------+------+------+------+------+-------+-------+---------+-------+


All releases are available as a Docker container, EC2 AMI, and a GCP image (GCP image from version 4.3).


ScyllaDB Enterprise
--------------------

.. note:: 
   Recommended OS and ScyllaDB AMI/Image OS for ScyllaDB Enterprise:

    - Ubuntu 20.04 for versions 2021.1 and later.
    - CentOS 7 for versions earlier than 2021.1.

+----------------------------+-----------------------------------+---------------------------+--------+-------+
| Linux Distributions        |  Ubuntu                           | Debian                    | CentOS/| Rocky/|
|                            |                                   |                           | RHEL   | RHEL  |
+----------------------------+------+------+------+------+-------+------+------+------+------+--------+-------+
| ScyllaDB Version / Version | 14.04| 16.04| 18.04| 20.04| 22.04 | 8    | 9    | 10   | 11   |  7     | 8     |
+============================+======+======+======+======+=======+======+======+======+======+========+=======+
|   2022.2                   | |x|  | |x|  | |v|  | |v|  | |v|   | |x|  | |x|  | |v|  | |v|  | |v|    | |v|   |
+----------------------------+------+------+------+------+-------+------+------+------+------+--------+-------+
|   2022.1                   | |x|  | |x|  | |v|  | |v|  | |x|   | |x|  | |x|  | |v|  | |v|  | |v|    | |v|   |
+----------------------------+------+------+------+------+-------+------+------+------+------+--------+-------+
|   2021.1                   | |x|  | |v|  | |v|  | |v|  | |x|   | |x|  | |v|  | |v|  | |x|  | |v|    | |v|   |
+----------------------------+------+------+------+------+-------+------+------+------+------+--------+-------+
|   2020.1                   | |x|  | |v|  | |v|  |  |x| | |x|   | |x|  | |v|  | |v|  | |x|  | |v|    | |v|   |
+----------------------------+------+------+------+------+-------+------+------+------+------+--------+-------+
|   2019.1                   | |x|  | |v|  | |v|  |  |x| | |x|   | |x|  | |v|  | |x|  | |x|  | |v|    | |x|   |
+----------------------------+------+------+------+------+-------+------+------+------+------+--------+-------+
|   2018.1                   | |v|  | |v|  | |x|  |  |x| | |v|   | |x|  | |x|  | |x|  | |x|  | |v|    | |x|   |
+----------------------------+------+------+------+------+-------+------+------+------+------+--------+-------+


All releases are available as a Docker container, EC2 AMI, and a GCP image (GCP image from version 2021.1).
