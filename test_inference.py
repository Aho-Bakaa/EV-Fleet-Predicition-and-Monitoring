from app.inference import EVMaintenancePredictor
import json

predictor = EVMaintenancePredictor()


sample_data = {
    'Vehicle_ID': 'VEH_TEST_001',
    
    'SOC': 0.75,
    'SOH': 0.88,
    'Charge_Cycles': 450.0,
    'Battery_Voltage': 360.5,
    'Battery_Current': -25.3,
    'Battery_Temperature': 42.5,
    'Battery_Health_Score': 0.87,
    'Battery_RUL_Cycles': 200.0,
    
    'Ambient_Temperature': 28.5,
    'Ambient_Humidity': 65.0,
    
    # Vehicle Operation
    'Load_Weight': 950.0,
    'Driving_Speed': 65.0,
    'Route_Roughness': 0.35,
    'Driver_Aggressiveness': 0.42,
    'Power_Consumption': 35.2,
    
    # Motor System
    'Motor_RPM': 3200.0,
    'Motor_Temperature': 75.5,
    'Motor_Torque': 180.0,
    'Motor_Health_Score': 0.89,
    
    # Inverter System
    'Inverter_Temperature': 68.3,
    'Inverter_Efficiency': 0.94,
    'Inverter_Health_Score': 0.91,
    
    # Thermal System
    'Coolant_Temperature': 55.2,
    'Pack_Temp_C': 42.5,
    'Thermal_System_Health_Score': 0.88,
    'Thermal_Gradient_Magnitude': 3.2,
    'Thermal_Runaway_Risk_Score': 0.025,
    
    # Transmission
    'Transmission_Temperature': 62.8,
    'Transmission_Efficiency': 0.96,
    
    # Braking & Recuperation
    'Energy_Recuperation_Rate': 0.18,
    'Brake_Pad_Wear': 0.35,
    'Reg_Brake_Efficiency': 0.75,
    
    # Suspension & Tires
    'Suspension_Load': 320.0,
    'Tire_Pressure': 32.5,
    'Tire_Temperature': 35.8,
    
    # Acceleration
    'Acceleration_X': 0.85,
    'Acceleration_Y': -0.12,
    'Acceleration_Z': 0.05,
    
    # Overall Health Scores
    'Charging_System_Health_Score': 0.90,
    'Component_Health_Score': 0.88,
    'Failure_Probability': 0.15,
    'Maintenance_Type': 0.0,
    
    # Vehicle State (mutually exclusive)
    'Is_Charging': 0,
    'Is_Discharging': 1,
    'Is_Idle': 0,
    
    # BMS Features - State of Power
    'SOP_Discharge_kW': 85.5,
    'SOP_Charge_kW': 45.2,
    
    # BMS Features - Degradation
    'Capacity_Fade_Rate': 0.28,
    
    # BMS Features - Safety
    'Lithium_Plating_Risk': 0.0,
    
    # BMS Features - Current & Power
    'Pack_Current_A': -25.3,
    'C_Rate': -0.506,
    'Pack_Internal_Resistance_Ohm': 0.045,
    
    # BMS Features - Cell Voltage
    'Max_Cell_Voltage_Diff': 0.025,
    'Cell_Voltage_Std': 0.008,
    'Cell_Voltage_Min': 3.65,
    'Cell_Voltage_Max': 3.68,
    'Cell_Voltage_Mean': 3.67,
    'Cell_Voltage_Std_Agg': 0.008,
    
    # BMS Features - Cell Temperature
    'Cell_Temp_Min': 41.2,
    'Cell_Temp_Max': 43.8,
    'Cell_Temp_Mean': 42.5,
    'Cell_Temp_Std': 0.85,
    
    # BMS Features - Cell Resistance
    'Cell_Resistance_Min': 2.45,
    'Cell_Resistance_Max': 2.85,
    'Cell_Resistance_Mean': 2.65,
    'Cell_Resistance_Std': 0.12,
    
    # BMS Features - Balancing
    'Cell_Balancing_Active': 0,
    'Balancing_Current_A': 0.0,
    
    # BMS Features - Charging History
    'Fast_Charging_Events_Count_1d': 2.0,
    'DCFC_Events_Count_1d': 0.0,
    
    # Temporal Features
    'Hour': 14,  # 2 PM
    'DayOfWeek': 3,  # Wednesday
    'DayOfYear': 287,  # October 14
    'Month': 10,
    'IsWeekend': 0,
    'IsNightTime': 0,
    'Timestamp_Unix': 1729767600.0,  # Oct 24, 2024 2:00 PM
    
    # One-Hot Encoded: Vehicle Type
    'Vehicle_Type_Delivery': 0,
    'Vehicle_Type_Personal': 0,
    'Vehicle_Type_Taxi': 1,
    
    # One-Hot Encoded: Weather
    'Weather_Condition_Foggy': 0,
    'Weather_Condition_Rainy': 0,
    'Weather_Condition_Sunny': 1,
    
    # One-Hot Encoded: Road Surface
    'Road_Surface_Condition_Icy': 0,
    'Road_Surface_Condition_Wet': 0,
    
    # One-Hot Encoded: Traffic
    'Traffic_Density_Low': 0,
    'Traffic_Density_Medium': 1
}

result = predictor.predict(sample_data)

print("\n" + "="*80)
print("PREDICTION RESULT")
print("="*80)
print(json.dumps(result, indent=2))
if result['status'] == 'success':
    print("\n" + "="*80)
    print("INTERPRETATION")
    print("="*80)
    
    pred = result['predictions']
    alert = result['alert']
    
    print(f"\n Battery Health:")
    print(f"   SOH: {pred['soh_percentage']}")
    print(f"   Remaining Life: {pred['rul_cycles']} cycles ({pred['rul_days']} days)")
    print(f"   Thermal Risk: {pred['thermal_risk_percentage']}")
    
    print(f"\n Alert Level: {alert['level']}")
    print(f"   {alert['message']}")
    
    if alert['actions']:
        print(f"\n Recommended Actions:")
        for i, action in enumerate(alert['actions'], 1):
            print(f"   {i}. {action}")
else:
    print(f"\n Error: {result['error_message']}")
