# FastMCP on Azure App Service
Deploying a Model Context Protocol (MCP) Server on Azure Using Python and FastMCP.

## Important Considerations

⚠️ **Cold Start Behavior**
- Azure App Service has a significant startup time when the instance is cold
- The first MCP request may fail or timeout if the instance is starting up
- **Recommendation**: Keep at least one instance always running to ensure reliable MCP responses

💡 **Best Practices**
- Configure **Always On** in your Azure App Service settings to prevent cold starts
- Consider using a higher pricing tier (Basic or above) for production workloads
- Monitor startup times and adjust the instance warm-up strategy as needed

## Installation

### Create Resources

1. **Create an Azure Web App**
   - Use the Azure Portal
   - or [Quickstart as Helper](https://learn.microsoft.com/en-us/azure/app-service/quickstart-python?tabs=fastapi%2Cwindows%2Cazure-portal%2Cazure-cli-deploy%2Cdeploy-instructions-azportal%2Cterminal-bash%2Cdeploy-instructions-zip-azcli)


### Deploy

#### Option 1: Deploy via Azure Pipeline
1. **Create a Service Connection in Azure DevOps**
   - Navigate to: **Project Settings** → **Service Connections** → **New Service Connection**
   - Select **Azure Resource Manager**
   - Choose the appropriate Subscription and Resource Group
2. **Create an Azure Pipeline**
   - In your Azure DevOps Project, navigate to: **Pipelines** → **New Pipeline**
   - Select your repository source (GitHub, Azure Repos, etc.)
   - Choose **Existing Azure Pipelines YAML file**
   - Select the `azure-pipelines.yml` file from this repository

3. **Configure Pipeline Variables**
   - Set the Azure Web App name and other required variables in the pipeline

4. **Run the Pipeline**
   - Save and run the pipeline to deploy the FastMCP application to Azure App Service

#### Option 2: Deploy via Command Line

1. **Login to Azure**
   ```bash
   az login
   ```

2. **Deploy to Azure App Service**
   ```bash
   az webapp up --name <your-app-name> --resource-group <your-resource-group> --runtime PYTHON:3.12
   ```

3. **Configure Startup Command**
   ```bash
   az webapp config set --name <your-app-name> --resource-group <your-resource-group> --startup-file startup.sh
   ```

## Test

Use the MCP Inspector to test: ```npx @modelcontextprotocol/inspector```


### Attachment
Sample applications are available for the other frameworks here:

* Django [https://github.com/Azure-Samples/msdocs-python-django-webapp-quickstart](https://github.com/Azure-Samples/msdocs-python-django-webapp-quickstart)
* FastAPI [https://github.com/Azure-Samples/msdocs-python-fastapi-webapp-quickstart](https://github.com/Azure-Samples/msdocs-python-fastapi-webapp-quickstart)

If you need an Azure account, you can [create one for free](https://azure.microsoft.com/en-us/free/).