
import subprocess
import osUtilities
import controller.yml.yamlUtilities as ymlUtils
import threading

class SolrServer(threading.Thread):
    """
    Solr Server Commands. Load parameters from model.solr.properties package.
    """
    params = ymlUtils.YamlUtilities()
    params.load(["core.sourcePaths", "solr.properties.solrServerProperties"])

    def __init__(self):
        """
        Initialize super depending on python version
        """
        if osUtilities.isPy32():
            super().__init__(name=self.params.get("title"))
        else:
            threading.Thread.__init__(self, name=self.params.get("title"))
        self._stop = threading.Event()

    def run(self):
        """
        starts the solr server
        """
        subprocess.call(self.params.get("startCmd"))

    def stop(self):
        self.shutdownSolr()
        self._stop.set()

    def stopped(self):
        return self._stop.isSet()

    def shutdownSolr(self):
        """
        stops the solr server and thread
        """
        print(self.params.get("shutdownCmd"))
        subprocess.call(self.params.get("shutdownCmd"))