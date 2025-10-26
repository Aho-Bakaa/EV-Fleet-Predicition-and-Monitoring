import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MODELS_DIR = BASE_DIR / "models"


SOH_MODEL_PATH = MODELS_DIR / "SOH_model.pkl"
SOH_SCALER_PATH = MODELS_DIR / "SOH_scaler.pkl"
RUL_MODEL_PATH = MODELS_DIR / "Battery_RUL_Cycles_model.pkl"
RUL_SCALER_PATH = MODELS_DIR / "Battery_RUL_Cycles_scaler.pkl"
THERMAL_MODEL_PATH = MODELS_DIR / "Thermal_Runaway_Risk_Score_model.pkl"
THERMAL_SCALER_PATH = MODELS_DIR / "Thermal_Runaway_Risk_Score_scaler.pkl"

# Model metadata
MODEL_VERSION = "1.0"
FEATURE_COLUMNS = [
    'SOC',
    'Charge_Cycles',
    'Battery_Voltage',
    'Battery_Current',
    'Battery_Temperature',
    'Ambient_Temperature',
    'Ambient_Humidity',
    'Load_Weight',
    'Driving_Speed',
    'Route_Roughness',
    'Driver_Aggressiveness',
    'Power_Consumption',
    'Motor_RPM',
    'Motor_Temperature',
    'Motor_Torque',
    'Inverter_Temperature',
    'Inverter_Efficiency',
    'Coolant_Temperature',
    'Transmission_Temperature',
    'Transmission_Efficiency',
    'Energy_Recuperation_Rate',
    'Brake_Pad_Wear',
    'Reg_Brake_Efficiency',
    'Suspension_Load',
    'Tire_Pressure',
    'Tire_Temperature',
    'Acceleration_X',
    'Acceleration_Y',
    'Acceleration_Z',
    'Battery_Health_Score',
    'Motor_Health_Score',
    'Inverter_Health_Score',
    'Thermal_System_Health_Score',
    'Charging_System_Health_Score',
    'Component_Health_Score',
    'Failure_Probability',
    'Is_Charging',
    'Is_Discharging',
    'Is_Idle',
    'SOP_Discharge_kW',
    'SOP_Charge_kW',
    'Capacity_Fade_Rate',
    'Lithium_Plating_Risk',
    'Pack_Current_A',
    'C_Rate',
    'Pack_Internal_Resistance_Ohm',
    'Pack_Temp_C',
    'Max_Cell_Voltage_Diff',
    'Cell_Voltage_Std',
    'Cell_Balancing_Active',
    'Balancing_Current_A',
    'Fast_Charging_Events_Count_1d',
    'DCFC_Events_Count_1d',
    'Thermal_Gradient_Magnitude',
    'Cell_Voltage_Min',
    'Cell_Voltage_Max',
    'Cell_Voltage_Mean',
    'Cell_Voltage_Std_Agg', 
    'Cell_Temp_Min',
    'Cell_Temp_Max',
    'Cell_Temp_Mean',
    'Cell_Temp_Std',
    'Cell_Resistance_Min',
    'Cell_Resistance_Max',
    'Cell_Resistance_Mean',
    'Cell_Resistance_Std',
    'Hour',
    'DayOfWeek',
    'DayOfYear',
    'Month',
    'IsWeekend',
    'IsNightTime',
    'Timestamp_Unix',
    'Vehicle_Type_Delivery',
    'Vehicle_Type_Personal',
    'Vehicle_Type_Taxi',
    'Weather_Condition_Foggy',
    'Weather_Condition_Rainy',
    'Weather_Condition_Sunny',
    'Road_Surface_Condition_Icy',
    'Road_Surface_Condition_Wet',
    'Traffic_Density_Low',
    'Traffic_Density_Medium'
]


#thresholds
SOH_CRITICAL_THRESHOLD = 0.80  
SOH_WARNING_THRESHOLD = 0.85
RUL_URGENT_THRESHOLD = 100  
THERMAL_DANGER_THRESHOLD = 0.70  
