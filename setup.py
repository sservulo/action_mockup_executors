from setuptools import setup

package_name = 'actionlib_proposal'

setup(
    name=package_name,
    version='0.5.1',
    packages=[],
    py_modules=[
	'action_client_executor',
	'action_server_executor'],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='Mikael Arguedas',
    author_email='mikael@osrfoundation.org',
    maintainer='Mikael Arguedas',
    maintainer_email='mikael@osrfoundation.org',
    keywords=['ROS'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='Actionlib proposal for Action server and client using rclpy.',
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'action_client_executor = action_client_executor:main',
            'action_server_executor = action_server_executor:main',
        ],
    },
)
