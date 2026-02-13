"""
First Aid Instructions Database
Source: Based on Red Cross and Mayo Clinic guidelines
"""

FIRST_AID_INSTRUCTIONS = {
    "minor_cut": {
        "name": "Minor Cut or Laceration",
        "severity": "low",
        "immediate_steps": [
            "Wash your hands thoroughly with soap and water",
            "Apply gentle pressure with a clean cloth to stop bleeding (5-10 minutes)",
            "Clean the wound gently with cool water - avoid hydrogen peroxide or iodine",
            "Apply antibiotic ointment if available",
            "Cover with a sterile bandage or clean cloth"
        ],
        "warning_signs": [
            "Bleeding doesn't stop after 10 minutes of pressure",
            "Cut is deep or has jagged edges",
            "Signs of infection: redness, swelling, warmth, pus, or red streaks",
            "Cut was caused by a dirty or rusty object",
            "Numbness or inability to move the affected area"
        ],
        "when_to_seek_help": "Seek immediate medical care if bleeding is heavy, the cut is deep, or you see any warning signs.",
        "additional_tips": [
            "Change bandage daily or if it gets wet",
            "Watch for signs of infection over the next few days",
            "Keep the wound clean and dry"
        ]
    },
    
    "burn": {
        "name": "Minor Burn (1st or 2nd Degree)",
        "severity": "medium",
        "immediate_steps": [
            "Remove from heat source immediately",
            "Cool the burn with cool (not ice-cold) running water for 10-20 minutes",
            "Remove jewelry or tight clothing near the burn before swelling starts",
            "Do NOT pop blisters - they protect against infection",
            "Cover loosely with sterile gauze or clean cloth",
            "Take over-the-counter pain reliever if needed (ibuprofen or acetaminophen)"
        ],
        "warning_signs": [
            "Burn is larger than 3 inches in diameter",
            "Burn is on face, hands, feet, genitals, or major joint",
            "Burn appears white, charred, or leathery (3rd degree)",
            "Victim is a child or elderly person",
            "Signs of infection develop",
            "Severe pain persists after initial cooling"
        ],
        "when_to_seek_help": "Go to emergency room immediately for burns larger than 3 inches, burns on sensitive areas, or any 3rd-degree burn.",
        "additional_tips": [
            "Never apply ice directly - it can cause further damage",
            "Avoid butter, oil, or ointments on fresh burns",
            "Keep burn clean and covered while healing"
        ]
    },
    
    "abrasion": {
        "name": "Abrasion or Scrape",
        "severity": "low",
        "immediate_steps": [
            "Wash hands before treating the wound",
            "Rinse the scrape with cool water for several minutes",
            "Gently clean around the wound with mild soap - don't scrub",
            "Remove any dirt or debris with clean tweezers",
            "Apply antibiotic ointment to keep surface moist",
            "Cover with bandage or sterile gauze"
        ],
        "warning_signs": [
            "Deep scrape with visible tissue or heavy bleeding",
            "Debris cannot be removed",
            "Signs of infection: increased redness, swelling, or pus",
            "Red streaks spreading from the wound",
            "Wound caused by an animal or human bite"
        ],
        "when_to_seek_help": "Seek medical care if the abrasion is deep, large, or shows signs of infection.",
        "additional_tips": [
            "Change bandage daily",
            "Watch for infection signs over 2-3 days",
            "If scab forms, leave it alone - it's part of healing"
        ]
    },
    
    "bruise": {
        "name": "Bruise or Contusion",
        "severity": "low",
        "immediate_steps": [
            "Apply ice pack wrapped in cloth for 15-20 minutes",
            "Elevate the bruised area above heart level if possible",
            "Rest the injured area",
            "Repeat icing every 2-3 hours for the first 24-48 hours",
            "After 48 hours, apply warm compresses to promote healing"
        ],
        "warning_signs": [
            "Severe pain or inability to move the area",
            "Bruising without known cause",
            "Bruising appears over a bone fracture",
            "Swelling is severe or increasing",
            "Signs of internal bleeding (dizziness, weakness, shortness of breath)",
            "Bruise doesn't improve after 2 weeks"
        ],
        "when_to_seek_help": "Seek immediate care if severe pain, swelling, or if bruise appeared without injury.",
        "additional_tips": [
            "Avoid aspirin as it can increase bleeding",
            "Gentle massage after 48 hours may help",
            "Color changes (purple to green/yellow) are normal healing"
        ]
    },
    
    "swelling": {
        "name": "Swelling or Inflammation",
        "severity": "medium",
        "immediate_steps": [
            "Follow R.I.C.E. protocol: Rest, Ice, Compression, Elevation",
            "Rest the affected area - avoid using it",
            "Apply ice pack for 15-20 minutes every 2-3 hours",
            "Use compression bandage (not too tight)",
            "Elevate above heart level when possible"
        ],
        "warning_signs": [
            "Swelling is severe or rapidly increasing",
            "Accompanied by severe pain",
            "Red streaks radiating from the area",
            "Warmth and redness suggesting infection",
            "Difficulty breathing or swelling in throat/face",
            "Swelling after an insect sting (possible allergic reaction)"
        ],
        "when_to_seek_help": "Seek emergency care immediately for facial/throat swelling, severe pain, or signs of allergic reaction.",
        "additional_tips": [
            "Remove jewelry before swelling increases",
            "Don't apply heat in first 48 hours",
            "If swelling persists beyond 48 hours, consult a doctor"
        ]
    },
    
    "unknown": {
        "name": "Unable to Classify Injury",
        "severity": "high",
        "immediate_steps": [
            "If there is bleeding, apply direct pressure with clean cloth",
            "Do not move the person if spinal injury is suspected",
            "Call emergency services (911 in US) immediately",
            "Keep the person calm and comfortable",
            "Do not give food or drink",
            "Monitor breathing and consciousness"
        ],
        "warning_signs": [
            "Any injury you're unsure how to treat",
            "Severe pain or distress",
            "Loss of consciousness",
            "Difficulty breathing",
            "Heavy bleeding",
            "Suspected broken bones or head injury"
        ],
        "when_to_seek_help": "Call emergency services immediately. When in doubt, always seek professional medical help.",
        "additional_tips": [
            "Stay with the person until help arrives",
            "Collect any information about how injury occurred",
            "If the person is unconscious, check for breathing and pulse"
        ]
    }
}

GENERAL_DISCLAIMER = """
⚠️ IMPORTANT MEDICAL DISCLAIMER

This tool provides GENERAL FIRST-AID GUIDANCE ONLY and is NOT a substitute for professional medical advice, diagnosis, or treatment.

• Always call emergency services (911 in US) for serious injuries
• Seek immediate medical care if you're unsure about severity
• This is temporary care guidance until professional help is available
• Different injuries may require different treatment - when in doubt, get professional help
• If symptoms worsen or don't improve, seek medical attention immediately

This tool cannot diagnose medical conditions. Trust your judgment and err on the side of caution.
"""

SAFETY_EXCLUSIONS = [
    "Head injuries or trauma",
    "Chest or abdominal wounds",
    "Severe bleeding that won't stop",
    "Suspected broken bones or fractures",
    "Eye injuries",
    "Electrical burns",
    "Chemical burns",
    "Animal or human bites",
    "Puncture wounds",
    "Any injury to an infant or very young child"
]
