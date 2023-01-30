from codecov_cli.helpers.ci_adapters.appveyor_ci import AppveyorCIAdapter
from codecov_cli.helpers.ci_adapters.azure_pipelines import AzurePipelinesCIAdapter
from codecov_cli.helpers.ci_adapters.buildkite import BuildkiteAdapter
from codecov_cli.helpers.ci_adapters.circleci import CircleCICIAdapter
from codecov_cli.helpers.ci_adapters.cirrus_ci import CirrusCIAdapter
from codecov_cli.helpers.ci_adapters.github_actions import GithubActionsCIAdapter
from codecov_cli.helpers.ci_adapters.gitlab_ci import GitlabCIAdapter
from codecov_cli.helpers.ci_adapters.heroku import HerokuCIAdapter
from codecov_cli.helpers.ci_adapters.jenkins import JenkinsAdapter


def get_ci_adapter(provider_name):
    if provider_name == "circleci":
        return CircleCICIAdapter()
    if provider_name == "githubactions":
        return GithubActionsCIAdapter()
    if provider_name == "gitlabCI":
        return GitlabCIAdapter()
    if provider_name == "appveyor":
        return AppveyorCIAdapter()
    if provider_name == "heroku":
        return HerokuCIAdapter()
    if provider_name == "buildkite":
        return BuildkiteAdapter()
    if provider_name == "azurepipelines":
        return AzurePipelinesCIAdapter()
    if provider_name == "jenkins":
        return JenkinsAdapter()
    if provider_name == "cirrusci":
        return CirrusCIAdapter()
    return None
