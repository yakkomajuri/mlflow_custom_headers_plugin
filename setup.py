from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="mlflow-custom-headers-plugin",
    version="1.0.1",
    description="MLFlow plugin that allows adding extra headers to requests to MLFlow in order to enable authentication and other use-cases.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Yakko Majuri",
    author_email="yakko.majuri@protonmail.com",
    license="MIT",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "mlflow>=2.8.0",
    ],
    python_requires=">=3.9",
    entry_points={
        "mlflow.request_header_provider": [
            "unused = mlflow_custom_headers_plugin.headers:CustomRequestHeaderProvider"
        ]
    },
    project_urls={
        "Source": "https://github.com/username/mlflow_custom_headers_plugin",
        "Bug Tracker": "https://github.com/username/mlflow_custom_headers_plugin/issues",
    },
)
