from pydantic import BaseModel, Field
from typing import Optional, List

class VehicleData(BaseModel):
    """
    Complete input schema for EV fleet data
    All 76 features from your preprocessed dataset
    """
    Vehicle_ID: str = Field(..., example="VEH_0001")
    SOC: float = Field(..., example=0.75)
    Charge_Cycles: float = Field(..., example=450.0)
    Battery_Voltage: float = Field(..., example=355.2)
    Battery_Current: float = Field(..., example=-45.3)
    Battery_Temperature: float = Field(..., example=42.5)
    Ambient_Temperature: float = Field(..., example=28.5)
    Ambient_Humidity: float = Field(..., example=65.0)
    Load_Weight: float = Field(..., example=950.0)
    Driving_Speed: float = Field(..., example=65.0)
    Route_Roughness: float = Field(..., example=0.25)
    Driver_Aggressiveness: float = Field(..., example=0.42)
    Power_Consumption: float = Field(..., example=35.5)
    Motor_RPM: float = Field(..., example=3200.0)
    Motor_Temperature: float = Field(..., example=78.5)
    Motor_Torque: float = Field(..., example=185.0)
    Inverter_Temperature: float = Field(..., example=55.2)
    Inverter_Efficiency: float = Field(..., example=0.94)
    Coolant_Temperature: float = Field(..., example=48.0)
    Transmission_Temperature: float = Field(..., example=62.5)
    Transmission_Efficiency: float = Field(..., example=0.96)
    Energy_Recuperation_Rate: float = Field(..., example=0.22)
    Brake_Pad_Wear: float = Field(..., example=0.35)
    Reg_Brake_Efficiency: float = Field(..., example=0.65)
    Suspension_Load: float = Field(..., example=320.0)
    Tire_Pressure: float = Field(..., example=32.5)
    Tire_Temperature: float = Field(..., example=38.0)
    Acceleration_X: float = Field(..., example=1.2)
    Acceleration_Y: float = Field(..., example=-0.3)
    Acceleration_Z: float = Field(..., example=0.1)
    Battery_Health_Score: float = Field(..., example=0.88)
    Motor_Health_Score: float = Field(..., example=0.92)
    Inverter_Health_Score: float = Field(..., example=0.94)
    Thermal_System_Health_Score: float = Field(..., example=0.90)
    Charging_System_Health_Score: float = Field(..., example=0.91)
    Component_Health_Score: float = Field(..., example=0.89)
    Failure_Probability: float = Field(..., example=0.15)
    Is_Charging: float = Field(..., example=0.0)
    Is_Discharging: float = Field(..., example=1.0)
    Is_Idle: float = Field(..., example=0.0)
    SOP_Discharge_kW: float = Field(..., example=85.0)
    SOP_Charge_kW: float = Field(..., example=50.0)
    Capacity_Fade_Rate: float = Field(..., example=0.25)
    Lithium_Plating_Risk: float = Field(..., example=0.0)
    Pack_Current_A: float = Field(..., example=-45.3)
    C_Rate: float = Field(..., example=-0.9)
    Pack_Internal_Resistance_Ohm: float = Field(..., example=0.045)
    Pack_Temp_C: float = Field(..., example=42.5)
    Max_Cell_Voltage_Diff: float = Field(..., example=0.16)
    Cell_Voltage_Std: float = Field(..., example=0.045)
    Cell_Balancing_Active: float = Field(..., example=0.0)
    Balancing_Current_A: float = Field(..., example=0.0)
    Fast_Charging_Events_Count_1d: float = Field(..., example=2.0)
    DCFC_Events_Count_1d: float = Field(..., example=0.0)
    Thermal_Gradient_Magnitude: float = Field(..., example=4.6)
    Cell_Voltage_Min: float = Field(..., example=3.42)
    Cell_Voltage_Max: float = Field(..., example=3.58)
    Cell_Voltage_Mean: float = Field(..., example=3.50)
    Cell_Voltage_Std_Agg: float = Field(..., example=0.045)
    Cell_Temp_Min: float = Field(..., example=40.2)
    Cell_Temp_Max: float = Field(..., example=44.8)
    Cell_Temp_Mean: float = Field(..., example=42.5)
    Cell_Temp_Std: float = Field(..., example=1.2)
    Cell_Resistance_Min: float = Field(..., example=2.6)
    Cell_Resistance_Max: float = Field(..., example=3.0)
    Cell_Resistance_Mean: float = Field(..., example=2.8)
    Cell_Resistance_Std: float = Field(..., example=0.12)
    Hour: float = Field(..., example=14.0)
    DayOfWeek: float = Field(..., example=3.0)
    DayOfYear: float = Field(..., example=287.0)
    Month: float = Field(..., example=10.0)
    IsWeekend: float = Field(..., example=0.0)
    IsNightTime: float = Field(..., example=0.0)
    Timestamp_Unix: float = Field(..., example=1729692000.0)
    Vehicle_Type_Delivery: Optional[float] = Field(0.0, example=0.0)
    Vehicle_Type_Personal: Optional[float] = Field(0.0, example=1.0)
    Vehicle_Type_Taxi: Optional[float] = Field(0.0, example=0.0)
    Weather_Condition_Foggy: Optional[float] = Field(0.0, example=0.0)
    Weather_Condition_Rainy: Optional[float] = Field(0.0, example=0.0)
    Weather_Condition_Sunny: Optional[float] = Field(0.0, example=1.0)
    Road_Surface_Condition_Icy: Optional[float] = Field(0.0, example=0.0)
    Road_Surface_Condition_Wet: Optional[float] = Field(0.0, example=0.0)
    Traffic_Density_Low: Optional[float] = Field(0.0, example=0.0)
    Traffic_Density_Medium: Optional[float] = Field(0.0, example=1.0)    
    class Config:
        json_schema_extra = {
            "example":{
  "Vehicle_ID": "VEH_0006",
  "Vehicle_Type": "Delivery",
  "Timestamp": "2023-07-01 15:15:00",
  "SOC": 0.1915506527471786,
  "Charge_Cycles": 169.79746337166205,
  "Battery_Voltage": 305.9506847576229,
  "Battery_Current": -211.0630595817153,
  "Battery_Temperature": 36.19687323475024,
  "Ambient_Temperature": 28.909296614496142,
  "Ambient_Humidity": 77.89587148787076,
  "Load_Weight": 88.0844638297671,
  "Driving_Speed": 0.0,
  "Timestamp": "2023-07-01 15:15:00",
  "Hour": 15,
  "DayOfWeek": 5,
  "DayOfYear": 182,
  "Month": 7,
  "IsWeekend": 0,
  "IsNightTime": 0,
  "Timestamp_Unix": 1688220900,
  "Route_Roughness": 0.0,
  "Driver_Aggressiveness": 0.2711996413666468,
  "Power_Consumption": 41.64144624938667,
  "Weather_Condition": "Sunny",
  "Road_Surface_Condition": "Dry",
  "Traffic_Density": "Medium",
  "Motor_RPM": 0.0,
  "Motor_Temperature": 28.909296614496142,
  "Motor_Torque": 0.0,
  "Inverter_Temperature": 42.07187179715236,
  "Inverter_Efficiency": 0.9517355167842512,
  "Coolant_Temperature": 33.634274813468465,
  "Transmission_Temperature": 29.120610291480315,
  "Transmission_Efficiency": 0.9749221980243538,
  "Energy_Recuperation_Rate": 0.1361717380944211,
  "Brake_Pad_Wear": 0.6058303688354546,
  "Reg_Brake_Efficiency": 0.3,
  "Lithium_Plating_Risk": 0.0,
  "Cell_Voltage_Std_Agg": 0.023,
  "Suspension_Load": 150.0,
  "Tire_Pressure": 30.079968345690663,
  "Tire_Temperature": 28.909296614496142,
  "Acceleration_X": 0.1035734873539709,
  "Acceleration_Y": 0.0027139132261346,
  "Acceleration_Z": 0.0465521839378811,
  "Battery_Health_Score": 0.9343779965178866,
  "Motor_Health_Score": 0.8230200209919284,
  "Inverter_Health_Score": 0.850761893140129,
  "Thermal_System_Health_Score": 0.9585491260157346,
  "Charging_System_Health_Score": 0.9030445477843048,
  "Component_Health_Score": 0.9073463044736176,
  "Failure_Probability": 0.0170345769753273,
  "Is_Charging": 1.0,
  "Is_Discharging": 0.0,
  "Is_Idle": 0.0,
  "SOP_Discharge_kW": 85.0,
  "SOP_Charge_kW": 50.0,
  "Capacity_Fade_Rate": 0.0708629089597759,
  "Pack_Current_A": -211.0630595817153,
  "C_Rate": -0.0042212611916343,
  "Pack_Internal_Resistance_Ohm": 0.0443881852130945,
  "Pack_Temp_C": 36.19687323475024,
  "Max_Cell_Voltage_Diff": 0.0,
  "Cell_Voltage_Std": 0.0,
  "Cell_Balancing_Active": 0.0,
  "Balancing_Current_A": 0.0,
  "Fast_Charging_Events_Count_1d": 0.0,
  "DCFC_Events_Count_1d": 0.0,
  "Thermal_Gradient_Magnitude": 13.209160401892165,
  "Cell_Voltage_Min": 4.25,
  "Cell_Voltage_Max": 4.25,
  "Cell_Voltage_Mean": 4.25,
  "Cell_Voltage_Std_Agg": 0.0,
  "Cell_Temp_Min": 36.02185733050823,
  "Cell_Temp_Max": 49.2310177324004,
  "Cell_Temp_Mean": 43.07593026961327,
  "Cell_Temp_Std": 4.594587423482057,
  "Cell_Resistance_Min": 3.245280812439092,
  "Cell_Resistance_Max": 4.463011234079197,
  "Cell_Resistance_Mean": 3.6990154344245423,
  "Cell_Resistance_Std": 0.361554852744427
}
        }
class Alert(BaseModel):
    level: str
    priority: int
    message: str
    actions:  List[str]
    color: Optional[str] = None


class Predictions(BaseModel):
    soh: float
    soh_percentage: str
    rul_cycles: int
    rul_days: int
    thermal_risk_score: float
    thermal_risk_percentage: str


class PredictionResponse(BaseModel):
    vehicle_id: str
    timestamp: str
    model_version: str
    predictions: Predictions
    alert: Alert
    status: str


class HealthResponse(BaseModel):
    status: str
    model_version: str
    timestamp: str


class ErrorResponse(BaseModel):
    status: str
    error_message: str
    timestamp: str
