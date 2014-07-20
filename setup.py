from distutils.core import setup
setup(name='CTS',
      version='0.0.0.1',
      author='Jonathan Prairie',
      author_email='augustus.seizure.1@gmail.com',
      license='None',
      description='Chess Tournament Simulator',
      long_description=open('README.md').read(),
      packages=['application', 'display', 'game_instance', 'options', 'player', 'stat_res', 'tournament'])