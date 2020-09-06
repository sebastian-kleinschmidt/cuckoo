class CockooPluginClass:
    """Example for a Cockoo Plugin"""
    pluginName = 'Testplugin'
    i = 12345

    def __init__(self):
        self.data = []

    def requestData(self):
	return '-Fetching Data'

    def visualizeContent(self):
	return '-Visualizing Content'

    def execute(self):
        return pluginName + ': Executing'
        self.requestData()
        self.visualizeContent()
	return pluginName + 'Finished'
