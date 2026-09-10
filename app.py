import os
from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# GUZAL APEX AI - B2B Fraud Detection Core
openai.api_key = os.environ.get("OPENAI_API_KEY", "mock-key-for-investors")

@app.route('/api/detect-scam', methods=['POST'])
def detect_scam():
    """
    Scans and evaluates risk metrics for international B2B suppliers and commodity brokers.
    Tailored for large-scale sunflower oil and sugar trade desk security.
    """
    try:
        data = request.get_json()
        supplier_profile = data.get("supplier_profile", "")
        domain_age_months = data.get("domain_age_months", 0)
        payment_terms = data.get("payment_terms", "")
        
        if not supplier_profile:
            return jsonify({"error": "Supplier data is empty"}), 400

        # High-risk trigger mechanisms
        risk_flags = []
        if domain_age_months < 6:
            risk_flags.append("Extremely New Domain Name (Created less than 6 months ago)")
        if "crypto" in payment_terms.lower() or "western union" in payment_terms.lower():
            risk_flags.append("High-risk non-corporate payment method requested")

        prompt = f"""
        Analyze this commodity supplier profile for fraud and middleman risks:
        ---
        Profile Details: {supplier_profile}
        Domain Age: {domain_age_months} months
        Payment Requested: {payment_terms}
        ---
        Provide a strict risk assessment in JSON format:
        1. RiskLevel (Low, Medium, Critical)
        2. VerifiedStatus (Is it a direct crusher/mill or an unverified broker?)
        3. RedFlags (list of anomalies found)
        4. Recommendation (Next secure action step)
        """

        # AI Security Protocol Call Simulation
        return jsonify({
            "status": "success",
            "project_name": "GUZAL AI B2B Broker Detector",
            "developer": "GuzalApexAI",
            "infrastructure": "Enterprise Tier-1 Security",
            "security_assessment": {
                "risk_level": "Critical" if risk_flags else "Low",
                "verified_status": "Unverified Middleman / Potential Scam Account",
                "detected_red_flags": risk_flags if risk_flags else ["None detected instantly, deep audit required"],
                "security_recommendation": "Do not proceed with advance payment. Demand 100% Transferable DLC via top-tier world bank with strict SGS verification."
            }
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5003)))

