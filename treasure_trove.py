import subprocess
subprocess.check_output('cli set cli screen-length 0', shell=True)
output = subprocess.check_output('cli help apropos .', shell=True)
output_list = output.split('\n')
help_topics = [line for line in output_list if line[0:10] == 'help topic']
for help_topic in help_topics:
    try:
        help = subprocess.check_output("cli " + help_topic, shell=True)
    except:
        continue
    if 'example: ' in help.lower():
        print(help_topic)