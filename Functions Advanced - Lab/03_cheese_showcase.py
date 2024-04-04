def sorting_cheeses(**kwargs):
    sorted_cheeses = sorted(kwargs.items(), key=lambda x: (-sum(x[1]), x[0]))
    return {cheese: sorted(quantities, reverse=True) for cheese, quantities in sorted_cheeses}
