.PHONY: install pipeline db dsa-test clean help

help: ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'

install: ## Install dependencies
	pip install -r requirements.txt

pipeline: ## Run the stock data ETL pipeline
	python -m stock_pipeline.pipeline

db: ## Run the DB setup, fetch live price, and plot
	python -m stock_pipeline.db

dsa-test: ## Quick-run all DSA solutions
	python -m dsa.two_sum
	python -m dsa.valid_palindrome
	python -m dsa.maximum_average_subarray

clean: ## Remove cached files and database
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	rm -f market_data.db
