"""
Equipment configuration for Service Reports
Defines equipment types and their inspection checklists
"""

EQUIPMENT_TYPES = {
    "KVF": {
        "name": "KVF Hood",
        "checklist": [
            {
                "id": "lights_operational",
                "question": "Are the hood lights operational?",
                "type": "yes_no_na",
                "conditions": {
                    "yes": {"photo": True},
                    "no": {"photo": True, "comment": True},
                    "n/a": {"comment": True}
                }
            },
            {
                "id": "lights_ballast",
                "question": "Is there a ballast for the Hood lights?",
                "type": "yes_no_na",
                "conditions": {
                    "yes": {
                        "follow_up": [
                            {
                                "id": "ballast_issue",
                                "question": "Is there an issue with the hood light ballast?",
                                "type": "yes_no_na",
                                "conditions": {
                                    "yes": {"photo": True, "comment": True},
                                    "no": {"photo": True, "comment": False},
                                    "n/a": {"comment": True}
                                }
                            }
                        ]
                    },
                    "no": {},
                    "n/a": {"comment": True}
                }
            },
            {
                "id": "capture_jet_fan",
                "question": "Is the capture jet fan working and in good condition?",
                "type": "yes_no_na",
                "conditions": {
                    "yes": {"photo": True},
                    "no": {"photo": True, "comment": True},
                    "n/a": {"comment": True}
                }
            },
            {
                "id": "extract_airflow_issue",
                "question": "Is there an issue in the hood extract airflow?",
                "type": "yes_no_na",
                "conditions": {
                    "yes": {
                        "comment": True,
                        "follow_up": [
                            {
                                "id": "extract_design_airflow",
                                "question": "Is the extract airflow achieving the design airflow?",
                                "type": "yes_no_na",
                                "conditions": {
                                    "yes": {},
                                    "no": {
                                        "photo": True,
                                        "comment": True,
                                        "follow_up": [
                                            {
                                                "id": "manual_damper",
                                                "question": "Is the manual damper fully opened?",
                                                "type": "yes_no_na",
                                                "conditions": {
                                                    "yes": {},
                                                    "no": {"photo": True, "comment": False, "action": "Please open the damper"},
                                                    "n/a": {"comment": True}
                                                }
                                            }
                                        ]
                                    }
                                }
                            }
                        ]
                    },
                    "no": {},
                    "n/a": {"comment": True}
                }
            },
            {
                "id": "supply_airflow_issue",
                "question": "Is there an issue in the hood supply airflow?",
                "type": "yes_no_na",
                "conditions": {
                    "yes": {
                        "comment": True,
                        "follow_up": [
                            {
                                "id": "supply_design_airflow",
                                "question": "Is the supply airflow achieving the design airflow?",
                                "type": "yes_no_na",
                                "conditions": {
                                    "yes": {},
                                    "no": {
                                        "photo": True,
                                        "comment": True,
                                        "follow_up": [
                                            {
                                                "id": "supply_manual_damper",
                                                "question": "Is the manual damper fully opened?",
                                                "type": "yes_no_na",
                                                "conditions": {
                                                    "yes": {},
                                                    "no": {"photo": True, "comment": False, "action": "Please open the damper"},
                                                    "n/a": {"comment": True}
                                                }
                                            }
                                        ]
                                    }
                                }
                            }
                        ]
                    },
                    "no": {},
                    "n/a": {"comment": True}
                }
            },
            {
                "id": "ksa_filters_condition",
                "question": "Are the KSA filters in good condition?",
                "type": "yes_no_na",
                "conditions": {
                    "yes": {"photo": True},
                    "no": {"photo": True, "comment": True},
                    "n/a": {"comment": True}
                }
            },
            {
                "id": "ksa_filters_in_place",
                "question": "Are the KSA filters all in place?",
                "type": "yes_no_na",
                "conditions": {
                    "yes": {"photo": True},
                    "no": {"photo": True, "comment": True},
                    "n/a": {"comment": True}
                }
            },
            {
                "id": "personal_supply_nozzles",
                "question": "Are the Personal supply air nozzles in place and in good condition?",
                "type": "yes_no_na",
                "conditions": {
                    "yes": {"photo": True},
                    "no": {"photo": True, "comment": True},
                    "n/a": {"comment": True}
                }
            },
            {
                "id": "other_issues",
                "question": "Do you have any comments about the hood condition, or anything noticed wrong with the hoods?",
                "type": "yes_no_na",
                "conditions": {
                    "yes": {
                        "comment": True,
                        "follow_up": [
                            {
                                "id": "issue_photos",
                                "question": "Do you want to include pictures for the issue witnessed?",
                                "type": "yes_no_na",
                                "conditions": {
                                    "yes": {},
                                    "no": {}
                                }
                            }
                        ]
                    },
                    "no": {},
                    "n/a": {"comment": True}
                }
            },
            {
                "id": "final_remarks",
                "question": "Do you want to add remarks on the KVF hood checked?",
                "type": "yes_no_na",
                "conditions": {
                    "yes": {"comment": True},
                    "no": {}
                }
            }
        ]
    },
    "KVI": {
        "name": "KVI Hood",
        "checklist": [
            {
                "id": "lights_operational",
                "question": "Are the hood lights operational?",
                "type": "yes_no_na",
                "conditions": {
                    "yes": {"photo": True},
                    "no": {"photo": True, "comment": True},
                    "n/a": {"comment": True}
                }
            },
            {
                "id": "lights_ballast",
                "question": "Is there a ballast for the Hood lights?",
                "type": "yes_no_na",
                "conditions": {
                    "yes": {
                        "follow_up": [
                            {
                                "id": "ballast_issue",
                                "question": "Is there an issue with the hood light ballast?",
                                "type": "yes_no_na",
                                "conditions": {
                                    "yes": {"photo": True, "comment": True},
                                    "no": {"photo": True, "comment": False},
                                    "n/a": {"comment": True}
                                }
                            }
                        ]
                    },
                    "no": {},
                    "n/a": {"comment": True}
                }
            },
            {
                "id": "capture_jet_fan",
                "question": "Is the capture jet fan working and in good condition?",
                "type": "yes_no_na",
                "conditions": {
                    "yes": {"photo": True},
                    "no": {"photo": True, "comment": True},
                    "n/a": {"comment": True}
                }
            },
            {
                "id": "extract_airflow_issue",
                "question": "Is there an issue in the hood extract airflow?",
                "type": "yes_no_na",
                "conditions": {
                    "yes": {
                        "comment": True,
                        "follow_up": [
                            {
                                "id": "extract_design_airflow",
                                "question": "Is the extract airflow achieving the design airflow?",
                                "type": "yes_no_na",
                                "conditions": {
                                    "yes": {},
                                    "no": {"photo": True, "comment": True},
                                    "n/a": {"comment": True}
                                }
                            }
                        ]
                    },
                    "no": {},
                    "n/a": {"comment": True}
                }
            },
            {
                "id": "ksa_filters_condition",
                "question": "Are the KSA filters in good condition?",
                "type": "yes_no_na",
                "conditions": {
                    "yes": {"photo": True},
                    "no": {"photo": True, "comment": True},
                    "n/a": {"comment": True}
                }
            },
            {
                "id": "ksa_filters_in_place",
                "question": "Are the KSA filters all in place?",
                "type": "yes_no_na",
                "conditions": {
                    "yes": {"photo": True},
                    "no": {"photo": True, "comment": True},
                    "n/a": {"comment": True}
                }
            },
            {
                "id": "blank_nozzles",
                "question": "Are the Blank nozzles in place and in good condition?",
                "type": "yes_no_na",
                "conditions": {
                    "yes": {"photo": True},
                    "no": {"photo": True, "comment": True},
                    "n/a": {"comment": True}
                }
            },
            {
                "id": "other_issues",
                "question": "Do you have any comments about the hood condition?",
                "type": "yes_no_na",
                "conditions": {
                    "yes": {
                        "comment": True,
                        "follow_up": [
                            {
                                "id": "issue_photos",
                                "question": "Do you want to include pictures for the issue witnessed?",
                                "type": "yes_no_na",
                                "conditions": {
                                    "yes": {},
                                    "no": {}
                                }
                            }
                        ]
                    },
                    "no": {},
                    "n/a": {"comment": True}
                }
            },
            {
                "id": "final_remarks",
                "question": "Do you want to add remarks on the KVI hood checked?",
                "type": "yes_no_na",
                "conditions": {
                    "yes": {"comment": True},
                    "no": {}
                }
            }
        ]
    },
    "UVF": {
        "name": "UVF Hood",
        "checklist": [
            {
                "id": "monitoring_console_type",
                "question": "What is the monitoring console type installed in the hood?",
                "type": "text",
                "required": True,
                "photo": True
            },
            {
                "id": "module_count",
                "question": "How many modules are connected to the monitoring system?",
                "type": "number",
                "required": True,
                "generates_modules": True
            },
            {
                "id": "alarms_registered",
                "question": "Is there an alarm registered in the monitoring console?",
                "type": "yes_no_na",
                "conditions": {
                    "yes": {
                        "follow_up": [
                            {
                                "id": "alarm_count",
                                "question": "How many alarms are registered?",
                                "type": "number",
                                "generates_alarms": True
                            }
                        ]
                    },
                    "no": {"photo": True, "comment": False}
                }
            },
            {
                "id": "uv_power_cable",
                "question": "Are the UV power cables in good condition?",
                "type": "yes_no_na",
                "conditions": {
                    "yes": {"photo": True},
                    "no": {"photo": True, "comment": True},
                    "n/a": {"comment": True}
                }
            },
            {
                "id": "ksa_filters_in_place",
                "question": "Are the KSA filters all in place?",
                "type": "yes_no_na",
                "conditions": {
                    "yes": {"photo": True},
                    "no": {"photo": True, "comment": True},
                    "n/a": {"comment": True}
                }
            },
            {
                "id": "filter_magnets",
                "question": "Are the filter magnets all in place?",
                "type": "yes_no_na",
                "conditions": {
                    "yes": {"photo": True},
                    "no": {"photo": True, "comment": True},
                    "n/a": {"comment": True}
                }
            },
            {
                "id": "lights_operational",
                "question": "Are the hood lights operational?",
                "type": "yes_no_na",
                "conditions": {
                    "yes": {"photo": True},
                    "no": {"photo": True, "comment": True},
                    "n/a": {"comment": True}
                }
            },
            {
                "id": "lights_ballast",
                "question": "Is there a ballast for the Hood lights?",
                "type": "yes_no_na",
                "conditions": {
                    "yes": {
                        "follow_up": [
                            {
                                "id": "ballast_issue",
                                "question": "Is there an issue with the hood light ballast?",
                                "type": "yes_no_na",
                                "conditions": {
                                    "yes": {"photo": True, "comment": True},
                                    "no": {"photo": True, "comment": False},
                                    "n/a": {"comment": True}
                                }
                            }
                        ]
                    },
                    "no": {},
                    "n/a": {"comment": True}
                }
            },
            {
                "id": "capture_jet_fan",
                "question": "Is the capture jet fan working and in good condition?",
                "type": "yes_no_na",
                "conditions": {
                    "yes": {"photo": True},
                    "no": {"photo": True, "comment": True},
                    "n/a": {"comment": True}
                }
            },
            {
                "id": "extract_airflow_issue",
                "question": "Is there an issue in the hood extract airflow?",
                "type": "yes_no_na",
                "conditions": {
                    "yes": {
                        "comment": True,
                        "follow_up": [
                            {
                                "id": "extract_design_airflow",
                                "question": "Is the extract airflow achieving the design airflow?",
                                "type": "yes_no_na",
                                "conditions": {
                                    "yes": {},
                                    "no": {
                                        "photo": True,
                                        "comment": True,
                                        "follow_up": [
                                            {
                                                "id": "manual_damper",
                                                "question": "Is the manual damper fully opened?",
                                                "type": "yes_no_na",
                                                "conditions": {
                                                    "yes": {},
                                                    "no": {"photo": True, "comment": False, "action": "Please open the damper"},
                                                    "n/a": {"comment": True}
                                                }
                                            }
                                        ]
                                    }
                                }
                            }
                        ]
                    },
                    "no": {},
                    "n/a": {"comment": True}
                }
            },
            {
                "id": "supply_airflow_issue",
                "question": "Is there an issue in the hood supply airflow?",
                "type": "yes_no_na",
                "conditions": {
                    "yes": {
                        "comment": True,
                        "follow_up": [
                            {
                                "id": "supply_design_airflow",
                                "question": "Is the supply airflow achieving the design airflow?",
                                "type": "yes_no_na",
                                "conditions": {
                                    "yes": {},
                                    "no": {
                                        "photo": True,
                                        "comment": True,
                                        "follow_up": [
                                            {
                                                "id": "supply_manual_damper",
                                                "question": "Is the manual damper fully opened?",
                                                "type": "yes_no_na",
                                                "conditions": {
                                                    "yes": {},
                                                    "no": {"photo": True, "comment": False, "action": "Please open the damper"},
                                                    "n/a": {"comment": True}
                                                }
                                            }
                                        ]
                                    }
                                }
                            }
                        ]
                    },
                    "no": {},
                    "n/a": {"comment": True}
                }
            },
            {
                "id": "other_issues",
                "question": "Do you have any comments about the hood condition?",
                "type": "yes_no_na",
                "conditions": {
                    "yes": {
                        "comment": True,
                        "follow_up": [
                            {
                                "id": "issue_photos",
                                "question": "Do you want to include pictures for the issue witnessed?",
                                "type": "yes_no_na",
                                "conditions": {
                                    "yes": {},
                                    "no": {}
                                }
                            }
                        ]
                    },
                    "no": {},
                    "n/a": {"comment": True}
                }
            },
            {
                "id": "final_remarks",
                "question": "Do you want to add remarks on the UVF hood checked?",
                "type": "yes_no_na",
                "conditions": {
                    "yes": {"comment": True},
                    "no": {}
                }
            }
        ]
    },
    "CMW": {
        "name": "CMW Hood (Cold Mist)",
        "checklist": [
            {
                "id": "lights_operational",
                "question": "Are the hood lights operational?",
                "type": "yes_no_na",
                "conditions": {
                    "yes": {"photo": True},
                    "no": {"photo": True, "comment": True},
                    "n/a": {"comment": True}
                }
            },
            {
                "id": "lights_ballast",
                "question": "Is there a ballast for the Hood lights?",
                "type": "yes_no_na",
                "conditions": {
                    "yes": {
                        "follow_up": [
                            {
                                "id": "ballast_issue",
                                "question": "Is there an issue with the hood light ballast?",
                                "type": "yes_no_na",
                                "conditions": {
                                    "yes": {"photo": True, "comment": True},
                                    "no": {"photo": True, "comment": False},
                                    "n/a": {"comment": True}
                                }
                            }
                        ]
                    },
                    "no": {},
                    "n/a": {"comment": True}
                }
            },
            {
                "id": "capture_jet_fan",
                "question": "Is the capture jet fan working and in good condition?",
                "type": "yes_no_na",
                "conditions": {
                    "yes": {"photo": True},
                    "no": {"photo": True, "comment": True},
                    "n/a": {"comment": True}
                }
            },
            {
                "id": "supply_air_connected",
                "question": "Does the hood have supply air connected?",
                "type": "yes_no_na",
                "conditions": {
                    "yes": {
                        "follow_up": [
                            {
                                "id": "supply_airflow_issue",
                                "question": "Is there an issue in the hood supply airflow?",
                                "type": "yes_no_na",
                                "conditions": {
                                    "yes": {
                                        "comment": True,
                                        "follow_up": [
                                            {
                                                "id": "supply_design_airflow",
                                                "question": "Is the supply airflow achieving the design airflow?",
                                                "type": "yes_no_na",
                                                "conditions": {
                                                    "yes": {},
                                                    "no": {
                                                        "photo": True,
                                                        "comment": True,
                                                        "follow_up": [
                                                            {
                                                                "id": "supply_manual_damper",
                                                                "question": "Is the manual damper fully opened?",
                                                                "type": "yes_no_na",
                                                                "conditions": {
                                                                    "yes": {},
                                                                    "no": {"photo": True, "comment": False, "action": "Please open the damper"}
                                                                }
                                                            }
                                                        ]
                                                    }
                                                }
                                            }
                                        ]
                                    },
                                    "no": {}
                                }
                            }
                        ]
                    },
                    "no": {},
                    "n/a": {"comment": True}
                }
            },
            {
                "id": "extract_airflow_issue",
                "question": "Is there an issue in the hood extract airflow?",
                "type": "yes_no_na",
                "conditions": {
                    "yes": {
                        "comment": True,
                        "follow_up": [
                            {
                                "id": "extract_design_airflow",
                                "question": "Is the extract airflow achieving the design airflow?",
                                "type": "yes_no_na",
                                "conditions": {
                                    "yes": {},
                                    "no": {
                                        "photo": True,
                                        "comment": True,
                                        "follow_up": [
                                            {
                                                "id": "manual_damper",
                                                "question": "Is the manual damper fully opened?",
                                                "type": "yes_no_na",
                                                "conditions": {
                                                    "yes": {},
                                                    "no": {"photo": True, "comment": False, "action": "Please open the damper"},
                                                    "n/a": {"comment": True}
                                                }
                                            }
                                        ]
                                    }
                                }
                            }
                        ]
                    },
                    "no": {},
                    "n/a": {"comment": True}
                }
            },
            {
                "id": "ksa_filters_condition",
                "question": "Are the KSA filters in good condition?",
                "type": "yes_no_na",
                "conditions": {
                    "yes": {"photo": True},
                    "no": {"photo": True, "comment": True},
                    "n/a": {"comment": True}
                }
            },
            {
                "id": "ksa_filters_in_place",
                "question": "Are the KSA filters all in place?",
                "type": "yes_no_na",
                "conditions": {
                    "yes": {"photo": True},
                    "no": {"photo": True, "comment": True},
                    "n/a": {"comment": True}
                }
            },
            {
                "id": "personal_supply_nozzles",
                "question": "Are the Personal supply air nozzles in place and in good condition?",
                "type": "yes_no_na",
                "conditions": {
                    "yes": {"photo": True},
                    "no": {"photo": True, "comment": True},
                    "n/a": {"comment": True}
                }
            },
            {
                "id": "cold_mist_nozzles_fully_operational",
                "question": "Are the cold mist nozzles fully operational and spraying?",
                "type": "yes_no_na",
                "conditions": {
                    "yes": {"photo": True},
                    "no": {"photo": True, "comment": True},
                    "n/a": {"comment": True}
                }
            },
            {
                "id": "solenoid_valve_cold_mist_operational",
                "question": "Are the solenoid valve for cold mist operational?",
                "type": "yes_no_na",
                "conditions": {
                    "yes": {"photo": True},
                    "no": {"photo": True, "comment": True},
                    "n/a": {"comment": True}
                }
            },
            {
                "id": "pressure_switch_operational_check",
                "question": "Is the pressure switch operational?",
                "type": "yes_no_na",
                "conditions": {
                    "yes": {"photo": True},
                    "no": {"photo": True, "comment": True},
                    "n/a": {"comment": True}
                }
            },
            {
                "id": "cold_mist_solenoid_coil_operational",
                "question": "Is the cold mist solenoid coil operational?",
                "type": "yes_no_na",
                "conditions": {
                    "yes": {"photo": True},
                    "no": {"photo": True, "comment": True},
                    "n/a": {"comment": True}
                }
            },
            {
                "id": "pressure_adjusted_halton",
                "question": "Is the pressure adjusted as per Halton recommended pressure?",
                "type": "yes_no_na",
                "conditions": {
                    "yes": {"photo": True},
                    "no": {"photo": True, "comment": True},
                    "n/a": {"comment": True}
                }
            },
            {
                "id": "hand_valve_fully_opened",
                "question": "Is the hand valve fully opened?",
                "type": "yes_no_na",
                "conditions": {
                    "yes": {"photo": True},
                    "no": {"photo": True, "comment": True},
                    "n/a": {"comment": True}
                }
            },
            {
                "id": "cold_water_available",
                "question": "Is there cold water available?",
                "type": "yes_no_na",
                "conditions": {
                    "yes": {"photo": True},
                    "no": {"photo": True, "comment": True},
                    "n/a": {"comment": True}
                }
            },
            {
                "id": "water_line_connected_properly",
                "question": "Is the water line connected properly?",
                "type": "yes_no_na",
                "conditions": {
                    "yes": {"photo": True},
                    "no": {"photo": True, "comment": True},
                    "n/a": {"comment": True}
                }
            },
            {
                "id": "water_leakage_witnessed",
                "question": "Is there any water leakage witnessed?",
                "type": "yes_no_na",
                "conditions": {
                    "yes": {"photo": True, "comment": True},
                    "no": {"photo": True},
                    "n/a": {"comment": True}
                }
            },
            {
                "id": "cold_mist_system",
                "question": "Does the system include cold mist with hot water wash?",
                "type": "yes_no_na",
                "conditions": {
                    "yes": {
                        "photo": True,
                        "comment": True,
                        "follow_up": [
                            {
                                "id": "power_supply",
                                "question": "Is there power supply available for the panel?",
                                "type": "yes_no_na",
                                "conditions": {
                                    "yes": {"photo": True},
                                    "no": {"photo": True, "comment": True},
                                    "n/a": {"comment": True}
                                }
                            },
                            {
                                "id": "hot_water_supply_hoods",
                                "question": "Is there hot water supply available for the hoods?",
                                "type": "yes_no_na",
                                "conditions": {
                                    "yes": {"photo": True},
                                    "no": {"photo": True, "comment": True},
                                    "n/a": {"comment": True}
                                }
                            },
                            {
                                "id": "solenoid_valve_hot_water",
                                "question": "Is the solenoid valve for the hot water working and in good condition?",
                                "type": "yes_no_na",
                                "conditions": {
                                    "yes": {"photo": True},
                                    "no": {"photo": True, "comment": True},
                                    "n/a": {"comment": True}
                                }
                            },
                            {
                                "id": "cold_mist_nozzle_count",
                                "question": "How many quantities of cold mist nozzles installed in the hood?",
                                "type": "number",
                                "required": True
                            },
                            {
                                "id": "cold_mist_nozzles_operational",
                                "question": "Are the cold mist nozzles all operational and in good condition?",
                                "type": "yes_no_na",
                                "conditions": {
                                    "yes": {"photo": True},
                                    "no": {"photo": True, "comment": True},
                                    "n/a": {"comment": True}
                                }
                            },
                            {
                                "id": "pressure_switch_operational",
                                "question": "Is the pressure switch operational?",
                                "type": "yes_no_na",
                                "conditions": {
                                    "yes": {
                                        "photo": True,
                                        "follow_up": [
                                            {
                                                "id": "pressure_switch_75pa",
                                                "question": "Is the pressure switch working on 75PA?",
                                                "type": "yes_no_na",
                                                "conditions": {
                                                    "yes": {"photo": True},
                                                    "no": {"comment": True}
                                                }
                                            }
                                        ]
                                    },
                                    "no": {"photo": True, "comment": True}
                                }
                            },
                            {
                                "id": "hot_water_supply",
                                "question": "Is the water supply available for hot water wash?",
                                "type": "yes_no_na",
                                "conditions": {
                                    "yes": {"photo": True},
                                    "no": {"photo": True, "comment": True},
                                    "n/a": {"comment": True}
                                }
                            },
                            {
                                "id": "hot_water_nozzles",
                                "question": "Are the hot water nozzles all working and in good condition?",
                                "type": "yes_no_na",
                                "conditions": {
                                    "yes": {"photo": True},
                                    "no": {"photo": True, "comment": True},
                                    "n/a": {"comment": True}
                                }
                            },
                            {
                                "id": "detergent_chemical",
                                "question": "Is the detergent chemical available and working?",
                                "type": "yes_no_na",
                                "conditions": {
                                    "yes": {
                                        "photo": True,
                                        "follow_up": [
                                            {
                                                "id": "detergent_chemical_full",
                                                "question": "Is the detergent chemical tank full?",
                                                "type": "yes_no_na",
                                                "conditions": {
                                                    "yes": {"photo": True},
                                                    "no": {"photo": True},
                                                    "n/a": {"comment": True}
                                                }
                                            }
                                        ]
                                    },
                                    "no": {"photo": True, "comment": True},
                                    "n/a": {"comment": True}
                                }
                            }
                        ]
                    },
                    "no": {},
                    "n/a": {"comment": True}
                }
            },
            {
                "id": "other_issues",
                "question": "Do you have any comments about the hood condition?",
                "type": "yes_no_na",
                "conditions": {
                    "yes": {
                        "comment": True,
                        "follow_up": [
                            {
                                "id": "issue_photos",
                                "question": "Do you want to include pictures for the issue witnessed?",
                                "type": "yes_no_na",
                                "conditions": {
                                    "yes": {"photo": True},
                                    "no": {}
                                }
                            }
                        ]
                    },
                    "no": {},
                    "n/a": {"comment": True}
                }
            },
            {
                "id": "final_remarks",
                "question": "Do you want to add remarks on the CMW hood checked?",
                "type": "yes_no_na",
                "conditions": {
                    "yes": {"comment": True},
                    "no": {}
                }
            }
        ]
    },
    "ECOLOGY": {
        "name": "Ecology Unit",
        "checklist": [
            {
                "id": "control_panel",
                "question": "Does the ecology unit have a control panel?",
                "type": "yes_no",
                "conditions": {
                    "yes": {
                        "follow_up": [
                            {
                                "id": "touch_screen_operational",
                                "question": "Is the Ecology unit touch screen operational and without alarms?",
                                "type": "yes_no",
                                "conditions": {
                                    "yes": {"photo": True},
                                    "no": {"photo": True, "comment": True}
                                }
                            }
                        ]
                    },
                    "no": {"comment": True}
                }
            },
            {
                "id": "vfd_running",
                "question": "Is the VFD running and in good condition?",
                "type": "yes_no",
                "conditions": {
                    "yes": {"photo": True, "comment": True},
                    "no": {"photo": True}
                }
            },
            {
                "id": "vfd_internal_components",
                "question": "Are the internal components of VFD operational and in good condition?",
                "type": "yes_no",
                "conditions": {
                    "yes": {"photo": True},
                    "no": {"photo": True, "comment": True}
                }
            },
            {
                "id": "esp_section",
                "question": "Is the ESP section available?",
                "type": "yes_no",
                "conditions": {
                    "yes": {
                        "follow_up": [
                            {
                                "id": "esp_working",
                                "question": "Is the ESP working and in good condition?",
                                "type": "yes_no",
                                "conditions": {
                                    "yes": {"photo": True},
                                    "no": {"photo": True, "comment": True}
                                }
                            },
                            {
                                "id": "hvps_working",
                                "question": "Is the HVPS working and in good condition?",
                                "type": "yes_no",
                                "conditions": {
                                    "yes": {"photo": True},
                                    "no": {"photo": True, "comment": True}
                                }
                            },
                            {
                                "id": "esp_autowash",
                                "question": "Is the ESP with autowash?",
                                "type": "yes_no",
                                "conditions": {
                                    "yes": {
                                        "photo": True,
                                        "follow_up": [
                                            {
                                                "id": "autowash_detergent",
                                                "question": "Does the autowash include detergent?",
                                                "type": "yes_no",
                                                "conditions": {
                                                    "yes": {"photo": True},
                                                    "no": {}
                                                }
                                            },
                                            {
                                                "id": "water_supply_available",
                                                "question": "Is the water supply available?",
                                                "type": "yes_no",
                                                "conditions": {
                                                    "yes": {},
                                                    "no": {"photo": True}
                                                }
                                            }
                                        ]
                                    },
                                    "no": {"photo": True, "comment": True}
                                }
                            }
                        ]
                    },
                    "no": {}
                }
            },
            {
                "id": "pre_filters_section",
                "question": "Is the PRE filters section available?",
                "type": "yes_no",
                "conditions": {
                    "yes": {
                        "follow_up": [
                            {
                                "id": "pre_filter_type",
                                "question": "What is the pre filters type?",
                                "type": "select",
                                "options": ["Washable", "Non-washable", "Both", "Other"],
                                "photo": True
                            },
                            {
                                "id": "pre_filters_quantity",
                                "question": "How many quantities of PRE filters?",
                                "type": "number"
                            },
                            {
                                "id": "pre_filters_dimensions",
                                "question": "What are the sizes/dimensions of the PRE Filters?",
                                "type": "text"
                            },
                            {
                                "id": "pre_filters_issue",
                                "question": "Is there an issue with PRE Filters?",
                                "type": "yes_no",
                                "conditions": {
                                    "yes": {"photo": True, "comment": True},
                                    "no": {"photo": True}
                                }
                            }
                        ]
                    },
                    "no": {}
                }
            },
            {
                "id": "bag_filters_section",
                "question": "Is the BAG Filters section available?",
                "type": "yes_no",
                "conditions": {
                    "yes": {
                        "follow_up": [
                            {
                                "id": "bag_filter_type",
                                "question": "What is the BAG filter type?",
                                "type": "select",
                                "options": ["ELF", "Normal"],
                                "photo": True
                            },
                            {
                                "id": "bag_filters_quantity",
                                "question": "How many quantities of BAG Filters?",
                                "type": "number"
                            },
                            {
                                "id": "bag_filters_dimensions",
                                "question": "What are the BAG Filters dimensions?",
                                "type": "text"
                            },
                            {
                                "id": "bag_filters_issue",
                                "question": "Is there an issue with BAG Filters?",
                                "type": "yes_no",
                                "conditions": {
                                    "yes": {"photo": True, "comment": True},
                                    "no": {"photo": True}
                                }
                            }
                        ]
                    },
                    "no": {}
                }
            },
            {
                "id": "hepa_filter_section",
                "question": "Is there HEPA Filter section available?",
                "type": "yes_no",
                "conditions": {
                    "yes": {
                        "follow_up": [
                            {
                                "id": "hepa_filter_type",
                                "question": "What is the HEPA Filter type?",
                                "type": "select",
                                "options": ["V-TYPE", "Normal", "Other"],
                                "photo": True
                            },
                            {
                                "id": "hepa_filters_quantity",
                                "question": "How many quantities of HEPA Filters?",
                                "type": "number"
                            },
                            {
                                "id": "hepa_filters_dimensions",
                                "question": "What are the dimensions of the HEPA Filters?",
                                "type": "text"
                            },
                            {
                                "id": "hepa_filters_issue",
                                "question": "Is there an issue with HEPA Filters?",
                                "type": "yes_no",
                                "conditions": {
                                    "yes": {"photo": True, "comment": True},
                                    "no": {"photo": True}
                                }
                            }
                        ]
                    },
                    "no": {}
                }
            },
            {
                "id": "carbon_filter_section",
                "question": "Is there Carbon filter section?",
                "type": "yes_no",
                "conditions": {
                    "yes": {
                        "follow_up": [
                            {
                                "id": "carbon_filter_type",
                                "question": "What is the Carbon filter type?",
                                "type": "select",
                                "options": ["V-TYPE", "Panel type", "Other"]
                            }
                        ]
                    },
                    "no": {}
                }
            },
            {
                "id": "uv_section",
                "question": "Is there UV Section in the ecology unit?",
                "type": "yes_no",
                "conditions": {
                    "yes": {
                        "follow_up": [
                            {
                                "id": "uv_tubes_issue",
                                "question": "Is there an issue with UV Tubes?",
                                "type": "yes_no",
                                "conditions": {
                                    "yes": {"photo": True, "comment": True},
                                    "no": {"photo": True}
                                }
                            },
                            {
                                "id": "uv_ballast_issue",
                                "question": "Is there an issue with UV ballast?",
                                "type": "yes_no",
                                "conditions": {
                                    "yes": {"photo": True, "comment": True},
                                    "no": {"photo": True}
                                }
                            },
                            {
                                "id": "uv_power_cables_issue",
                                "question": "Is there an issue with the UV Power cables?",
                                "type": "yes_no",
                                "conditions": {
                                    "yes": {"photo": True, "comment": True},
                                    "no": {"photo": True}
                                }
                            }
                        ]
                    },
                    "no": {}
                }
            },
            {
                "id": "other_comments",
                "question": "Do you have any comments on ecology unit other than above?",
                "type": "yes_no",
                "conditions": {
                    "yes": {
                        "comment": True,
                        "follow_up": [
                            {
                                "id": "comment_photos",
                                "question": "Do you want to add pics?",
                                "type": "yes_no",
                                "conditions": {
                                    "yes": {"photo": True},
                                    "no": {}
                                }
                            }
                        ]
                    },
                    "no": {}
                }
            }
        ]
    },
    "MOBICHEF": {
        "name": "Mobichef",
        "checklist": [
            {
                "id": "hood_lights",
                "question": "Hood lights are working and in good condition?",
                "type": "yes_no_na",
                "conditions": {
                    "yes": {"photo": True},
                    "no": {"photo": True, "comment": True},
                    "n/a": {"comment": True}
                }
            },
            {
                "id": "ksa_filters",
                "question": "All KSA filters are in place and in good condition?",
                "type": "yes_no_na",
                "conditions": {
                    "yes": {"photo": True},
                    "no": {"photo": True, "comment": True},
                    "n/a": {"comment": True}
                }
            },
            {
                "id": "mesh_filters",
                "question": "All Mesh filters are in place and in good conditions?",
                "type": "yes_no_na",
                "conditions": {
                    "yes": {"photo": True},
                    "no": {"photo": True, "comment": True},
                    "n/a": {"comment": True}
                }
            },
            {
                "id": "pre_filters",
                "question": "PRE Filters are in place and in good condition?",
                "type": "yes_no_na",
                "conditions": {
                    "yes": {"photo": True},
                    "no": {"photo": True, "comment": True},
                    "n/a": {"comment": True}
                }
            },
            {
                "id": "esp_working",
                "question": "ESP is working and in good condition?",
                "type": "yes_no_na",
                "conditions": {
                    "yes": {"photo": True},
                    "no": {"photo": True, "comment": True},
                    "n/a": {"comment": True}
                }
            },
            {
                "id": "carbon_filters",
                "question": "Carbon filters are in place and in good condition?",
                "type": "yes_no_na",
                "conditions": {
                    "yes": {"photo": True},
                    "no": {"photo": True, "comment": True},
                    "n/a": {"comment": True}
                }
            },
            {
                "id": "capture_jet_fan",
                "question": "Capture jet fans are working and in good condition?",
                "type": "yes_no_na",
                "conditions": {
                    "yes": {"photo": True},
                    "no": {"photo": True, "comment": True},
                    "n/a": {"comment": True}
                }
            },
            {
                "id": "touch_screen",
                "question": "Touch screen is operational without any alarms?",
                "type": "yes_no_na",
                "conditions": {
                    "yes": {"photo": True},
                    "no": {"photo": True, "comment": True},
                    "n/a": {"comment": True}
                }
            },
            {
                "id": "other_issues",
                "question": "Do you have any comments about the Mobichef System?",
                "type": "yes_no_na",
                "conditions": {
                    "yes": {
                        "comment": True,
                        "follow_up": [
                            {
                                "id": "issue_photos",
                                "question": "Do you want to include pictures for the issue witnessed?",
                                "type": "yes_no_na",
                                "conditions": {
                                    "yes": {},
                                    "no": {}
                                }
                            }
                        ]
                    },
                    "no": {},
                    "n/a": {"comment": True}
                }
            },
            {
                "id": "final_remarks",
                "question": "Do you want to add remarks on the Mobichef System checked?",
                "type": "yes_no_na",
                "conditions": {
                    "yes": {"comment": True},
                    "no": {}
                }
            }
        ]
    }
}

# MARVEL System checklist (used when "With Marvel" checkbox is selected)
MARVEL_CHECKLIST = [
    {
        "id": "power_supply",
        "question": "Power supply is available for marvel control panel?",
        "type": "yes_no_na",
        "conditions": {
            "yes": {"photo": True},
            "no": {"photo": True, "comment": True},
            "n/a": {"comment": True}
        }
    },
    {
        "id": "touch_screen_operational",
        "question": "Marvel touch screen is operating and without alarms?",
        "type": "yes_no_na",
        "conditions": {
            "yes": {"photo": True},
            "no": {"photo": True, "comment": True},
            "n/a": {"comment": True}
        }
    },
    {
        "id": "internal_components",
        "question": "All internal components inside MARVEL panel are operational?",
        "type": "yes_no_na",
        "conditions": {
            "yes": {"photo": True},
            "no": {"comment": True},
            "n/a": {"comment": True}
        }
    },
    {
        "id": "signals_vfd",
        "question": "(0-10V) Signals are being sent from Marvel system and VFD is responding properly?",
        "type": "yes_no_na",
        "conditions": {
            "yes": {"photo": True},
            "no": {"comment": True},
            "n/a": {"comment": True}
        }
    },
    {
        "id": "ntc_sensors",
        "question": "All NTC sensors are working and in good condition?",
        "type": "yes_no_na",
        "conditions": {
            "yes": {"photo": True},
            "no": {"photo": True, "comment": True},
            "n/a": {"comment": True}
        }
    },
    {
        "id": "ir_sensors",
        "question": "All IR Sensors are working and in good condition?",
        "type": "yes_no_na",
        "conditions": {
            "yes": {"photo": True},
            "no": {"photo": True, "comment": True},
            "n/a": {"comment": True}
        }
    },
    {
        "id": "abd_dampers",
        "question": "ABD Dampers are operating properly and without any alarms?",
        "type": "yes_no_na",
        "conditions": {
            "yes": {"photo": True},
            "no": {"photo": True, "comment": True},
            "n/a": {"comment": True}
        }
    },
    {
        "id": "abd_actuators",
        "question": "All ABD Actuators are working and in good condition?",
        "type": "yes_no_na",
        "conditions": {
            "yes": {"photo": True},
            "no": {"photo": True, "comment": True},
            "n/a": {"comment": True}
        }
    },
    {
        "id": "other_issues",
        "question": "Do you have any comments about the MARVEL System?",
        "type": "yes_no",
        "conditions": {
            "yes": {
                "comment": True,
                "follow_up": [
                    {
                        "id": "issue_photos",
                        "question": "Do you want to include pictures for the issue witnessed?",
                        "type": "yes_no_na",
                        "conditions": {
                            "yes": {"photo": True},
                            "no": {}
                        }
                    }
                ]
            },
            "no": {}
        }
    },
    {
        "id": "final_remarks",
        "question": "Do you want to add remarks on the MARVEL System checked?",
        "type": "yes_no",
        "conditions": {
            "yes": {"comment": True},
            "no": {}
        }
    }
]

# Module checklist for UVF hoods
UVF_MODULE_CHECKLIST = [
    {
        "id": "uv_cassettes",
        "question": "Please take picture of the UV cassettes showing the number of tubes",
        "type": "photo",
        "required": True
    },
    {
        "id": "ksa_filter_magnets",
        "question": "Please take pictures of the KSA filters magnets",
        "type": "photo",
        "required": True
    },
    {
        "id": "ksa_filter_dimensions",
        "question": "What is the dimensions of the KSA filter?",
        "type": "text",
        "required": True
    },
    {
        "id": "uv_door_sensor",
        "question": "Please take pictures of the UV Door sensor and UV door magnet",
        "type": "photo",
        "required": True
    },
    {
        "id": "uv_controllers",
        "question": "Please take pictures of the UV controllers MU1 & VV1",
        "type": "photo",
        "required": True
    },
    {
        "id": "pressure_tube_connection",
        "question": "Please take pictures of the connection of the pressure tube from controller side and plenum side",
        "type": "photo",
        "required": True
    },
    {
        "id": "uv_ballast",
        "question": "Please take pictures of the UV ballast",
        "type": "photo",
        "required": True
    },
    {
        "id": "uv_pcb_board",
        "question": "Please take pictures of the UV pcb board",
        "type": "photo",
        "required": True
    },
    {
        "id": "uv_power_cable",
        "question": "Please take pictures of the UV power cable and from cassette connection",
        "type": "photo",
        "required": True
    },
    {
        "id": "filter_count",
        "question": "How many filters are installed in this module?",
        "type": "number",
        "required": True
    },
    {
        "id": "module_alarm",
        "question": "Is the alarm registered for this module?",
        "type": "yes_no",
        "conditions": {
            "yes": {
                "follow_up": [
                    {
                        "id": "alarm_reason",
                        "question": "What is the reason the alarm is triggered?",
                        "type": "select",
                        "options": ["UV system", "Communication", "Airflow/safety interlock switches"],
                        "photo": True,
                        "comment": True
                    },
                    {
                        "id": "alarm_fixable",
                        "question": "Can the alarm be fixed and removed from the screen on site?",
                        "type": "yes_no_na",
                        "conditions": {
                            "yes": {"photo": True},
                            "no": {"comment": True}
                        }
                    }
                ]
            },
            "no": {}
        }
    },
    {
        "id": "broken_uv_tube",
        "question": "Is there a broken UV tube witnessed in this module?",
        "type": "yes_no",
        "conditions": {
            "yes": {"photo": True, "comment": True},
            "no": {"photo": True}
        }
    }
]

# PPM Checklist (for AMC contracts)
PPM_CHECKLIST = [
    {
        "id": "hood_light_cleaned",
        "question": "Is the hood light cleaned?",
        "type": "yes_no"
    },
    {
        "id": "capture_jet_fan_cleaned",
        "question": "Is the capture jet fan cleaned?",
        "type": "yes_no"
    },
    {
        "id": "hood_plenum_cleaned",
        "question": "Is the hood plenum cleaned?",
        "type": "yes_no"
    },
    {
        "id": "before_after_photos_count",
        "question": "How many before and after pictures do you want to include?",
        "type": "number",
        "generates_photo_pairs": True
    },
    {
        "id": "ppm_comments",
        "question": "Do you have any comments about the PPM Implemented?",
        "type": "yes_no",
        "conditions": {
            "yes": {
                "photo": True,
                "comment": True,
                "follow_up": [
                    {
                        "id": "ppm_issue_photos",
                        "question": "Do you want to include pictures for the issue witnessed?",
                        "type": "yes_no_na",
                        "conditions": {
                            "yes": {"photo": True},
                            "no": {}
                        }
                    }
                ]
            },
            "no": {}
        }
    },
    {
        "id": "ppm_remarks",
        "question": "Do you want to add remarks?",
        "type": "yes_no",
        "conditions": {
            "yes": {"comment": True},
            "no": {}
        }
    }
]

# UV System specific PPM items
UV_PPM_ITEMS = [
    {
        "id": "uv_cassette_cleaned",
        "question": "Is the UV cassette cleaned?",
        "type": "yes_no"
    },
    {
        "id": "uv_lamps_cleaned",
        "question": "Are the UV Lamps cleaned?",
        "type": "yes_no"
    },
    {
        "id": "uv_door_cleaned",
        "question": "Is the UV Door cleaned?",
        "type": "yes_no"
    }
]

# Water wash system PPM items
WATER_WASH_PPM_ITEMS = [
    {
        "id": "cold_water_nozzles_cleaned",
        "question": "Are the nozzles for cold water cleaned?",
        "type": "yes_no"
    },
    {
        "id": "hot_water_nozzles_cleaned",
        "question": "Are the nozzles for hot water cleaned (if available)?",
        "type": "yes_no"
    }
]

# Ecology specific PPM items
ECOLOGY_PPM_ITEMS = [
    {
        "id": "ecology_filters_cleaned",
        "question": "Are the Ecology filters cleaned and in good condition?",
        "type": "yes_no",
        "conditions": {
            "yes": {"photo": True},
            "no": {"photo": True, "comment": True}
        }
    },
    {
        "id": "ecology_unit_cleaned",
        "question": "Is the Ecology unit cleaned?",
        "type": "yes_no",
        "conditions": {
            "yes": {"photo": True},
            "no": {"photo": True, "comment": True}
        }
    },
    {
        "id": "vfd_panel_cleaned",
        "question": "Is the VFD panel cleaned?",
        "type": "yes_no",
        "conditions": {
            "yes": {"photo": True},
            "no": {"photo": True, "comment": True}
        }
    },
    {
        "id": "vfd_operational",
        "question": "Is the VFD operational and in good condition?",
        "type": "yes_no",
        "conditions": {
            "yes": {"photo": True},
            "no": {"photo": True, "comment": True}
        }
    },
    {
        "id": "ecology_fan_cleaned",
        "question": "Is the ecology fan cleaned and in good condition?",
        "type": "yes_no",
        "conditions": {
            "yes": {"photo": True},
            "no": {"photo": True, "comment": True}
        }
    },
    {
        "id": "ecology_motor_cleaned",
        "question": "Is the ecology unit motor cleaned and in good condition?",
        "type": "yes_no",
        "conditions": {
            "yes": {"photo": True},
            "no": {"photo": True, "comment": True}
        }
    }
]