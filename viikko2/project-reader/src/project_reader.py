from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        t_dict = toml.loads(content)
        name = t_dict["tool"]["poetry"]["name"]
        description = t_dict["tool"]["poetry"]["description"]
        license = t_dict["tool"]["poetry"]["license"]

        authors = t_dict["tool"]["poetry"]["authors"]

        dependencies = t_dict["tool"]["poetry"]["dependencies"]

        dev_dependencies = t_dict["tool"]["poetry"]["group"]["dev"]["dependencies"]

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, license, authors, dependencies, dev_dependencies)