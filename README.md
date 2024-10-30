# MLFlow Custom Headers Plugin

> [Source code](https://github.com/yakkomajuri/mlflow_custom_headers_plugin)

A package that enables setting any number of custom headers to be passed along with requests to the MLFlow tracking server.

This is very useful for enabling proper authentication on your MLFlow instance beyond MLFlow's simplistic authentication capabilities using basic auth or one single token.

This plugin was inspired by the [mlflow-cloudflare-header-plugin](https://pypi.org/project/mlflow-cloudflare-header-plugin/) and does also provide support for using Cloudflare Access service tokens for securing your MLFlow tracking server.

## Usage

Install the plugin in your project using MLFlow:

```bash
pip install mlflow-custom-headers-plugin
```

Set all the headers you'd like passed in an environment variable called `MLFLOW_CUSTOM_HEADERS`. Key-value header pairs should be separated by commas, and header name and value should be separated by a colon (`:`) without any empty space.

```
export MLFLOW_CUSTOM_HEADERS=Header1:<Header1Value>,Header2:<Header2Value>,Header3:<Header2Value>
```

Example (using Cloudflare Access):

```
export MLFLOW_CUSTOM_HEADERS=CF-Access-Client-Id:<cf_client_id>,CF-Access-Client-Secret:<cf_client_secret>
```


