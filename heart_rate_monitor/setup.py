from setuptools import find_packages, setup

package_name = 'heart_rate_monitor'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='sck2n21',
    maintainer_email='sck2n21@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "heart_rate = heart_rate_monitor.heart_rate_monitor_node:main"
            "finger_detect = heart_rate_monitor.finger_detect:main"
        ],
    },
)
