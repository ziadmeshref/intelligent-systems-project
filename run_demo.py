from src.integration import WarehousePipeline

def main():
    print("Initializing Warehouse Re-Slotting Pipeline...")
    pipeline = WarehousePipeline()
    
    print("\n--- Step 1: NN Demand Forecasting ---")
    demand = pipeline.forecast_demand()
    
    print("\n--- Step 2: CSP Initial Layout ---")
    initial_layout = pipeline.generate_initial_layout(demand)
    
    print("\n--- Step 3: Search for Layout Improvements ---")
    final_layout = pipeline.optimize_layout_with_search(initial_layout)
    
    print("\n--- Step 4: Evaluate on Real Orders ---")
    pipeline.evaluate_picker_distance(final_layout)

if __name__ == '__main__':
    main()
