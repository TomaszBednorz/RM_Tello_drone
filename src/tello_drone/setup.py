from setuptools import setup

package_name = 'tello_drone'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ubuntu-20-04-vm',
    maintainer_email='tomekbed99@gmail.com',
    description='Tello drone',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'service = tello_drone.tello_service:main',
            'client = tello_drone.tello_client:main',
        ],
    },
)
