class Config:
    '''
    General configuration parent class
    '''
    ApiUrl='https://newsapi.org/v2/everything?q=apple&apiKey=338b3acd04e94ca08029f617b628e5b4'




class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True