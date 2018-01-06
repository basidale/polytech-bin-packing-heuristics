from stat_scenario import StatExecutionScenario

class StatMode:
    add_scenario_dialog_msg = '\nAdd a scenario? (0=NO 1=yes)'
    
    def __init__(self):
        self.scenarios = list()

    def start(self):
        self.openDialog()

        while self.askForANewScenario():
            self.openDialog()
        
        for scenario in self.scenarios:
            scenario.execute()

    def askForANewScenario(self):
        print(self.add_scenario_dialog_msg)
        return True if input('> ') == '1' else False
                
    def openDialog(self):
        scenario = StatExecutionScenario()
        scenario.openDialog()
        self.scenarios.append(scenario)
    
