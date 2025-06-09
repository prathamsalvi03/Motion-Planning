from setuptools import setup

package_name = 'panda_vision'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='pratham',
    maintainer_email='your@email.com',
    description='Vision-based object detection for planning',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'vision_node = panda_vision.vision_node:main',
        ],
    },
)