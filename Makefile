.PHONY: command_server
command_server:
	cmd /C "set PYTHONPATH=lib && python lib/send_command_to_server.py"

.PHONY: test-challenges
test-challenges:
	cmd /C "set PYTHONPATH=lib/solutions/ && pytest test/unit/challenges"
