from stat_scenario import StatExecutionScenario

class StatMode:
    def __init__(self):
        self.scenarios = list()

    def select(self):
        addScenario = True

        while addScenario:
            if len(self.scenarios) > 0:
                print('')
                print('Add a scenario? (0=NO 1=yes)')
                addScenario = True if input('> ') == '1' else False

            if addScenario:
                scenario = StatExecutionScenario()
                scenario.openDialog()
                self.scenarios.append(scenario)            
        
        for scenario in self.scenarios:
            scenario.execute()

        

