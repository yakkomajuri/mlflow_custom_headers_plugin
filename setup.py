from setuptools import setup, find_packages

setup(
    name="mlflow-custom-headers-plugin",
    version="1.0.0",
    description="MLFlow plugin that allows adding extra headers to requests to MLFlow in order to enable authentication and other use-cases.",
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
)
