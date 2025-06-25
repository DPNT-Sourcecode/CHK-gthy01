.PHONY: test-challenges
test-challenges:
	cmd /C "set PYTHONPATH=challenges && pytest test/unit/challenges"