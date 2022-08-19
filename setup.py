from setuptools import setup

setup(
    name="typewriter-cli",
    version="0.1",
    py_modules=["typewriter"],
    include_package_data=True,
    install_requires=["click", "openai"],
    entry_points="""
        [console_scripts]
        typewriter=typewriter:cli
    """,
)