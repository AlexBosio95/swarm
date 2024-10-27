from swarm import Swarm, Agent
from flask import Flask, request, render_template, session
import json

client = Swarm()

app = Flask(__name__)
app.secret_key = 'Uz56B(R"up@*#NP!RYU)<MjIq1{sy:'

# Definizione delle funzioni degli agenti
def handle_payments():
    return "The payment options include credit card, PayPal, and bank transfer."

def provide_policy_information():
    return "Our return policy allows for returns within 30 days of purchase."

def list_products():
    return [
        "Website Development",
        "E-commerce Development",
        "UX/UI Design",
        "SEO (Search Engine Optimization)",
        "Digital Marketing",
        "Social Media Management",
        "Content Creation",
        "Branding and Visual Identity",
        "Performance Analysis and Reporting",
        "Technical Support and Maintenance",
        "Digital Strategy Consulting",
        "Advertising Campaign Management (Google Ads, Facebook Ads)",
        "Website Speed Optimization",
        "CRM System Integration"
    ]

def check_warehouse_status():
    return "The product is currently in stock and ready for shipping."

def handle_technical_support():
    return "For technical issues, please restart your device and ensure all updates are installed."

def handle_account_issues():
    return "For account-related issues, such as password reset or account recovery, please provide your registered email."

def handle_feedback():
    return "Thank you for your feedback. We strive to improve our services based on customer input."

def handle_appointment_booking():
    return "Please provide your preferred date and time for booking an appointment with our consultant."

def handle_billing_queries():
    return "For billing queries, please provide your invoice number and details of the charges in question."

def create_order():
    return "Order creation initiated. Please provide product details and quantity."

def create_jira_task():
    return "A Jira task has been created for processing the order."

def create_quote():
    return "A quote has been generated based on the product list and pricing. Please provide the details of the items you need."

def transfer_to_payments_agent():
    return payments_agent

def transfer_to_policy_agent():
    return policy_agent

def transfer_to_sales_product_agent():
    return sales_product_agent

def transfer_to_warehouse_agent():
    return warehouse_agent

def transfer_to_technical_support_agent():
    return technical_support_agent

def transfer_to_account_agent():
    return account_agent

def transfer_to_feedback_agent():
    return feedback_agent

def transfer_to_appointment_agent():
    return appointment_agent

def transfer_to_billing_agent():
    return billing_agent

def transfer_to_jira_agent():
    return jira_agent

def transfer_to_quote_agent():
    return quote_agent

# Definizione degli agenti
customer_care_agent = Agent(
    name="Customer Care Agent",
    instructions="You are the main customer care AI, Always respond in English, that redirects requests to the appropriate agent based on user queries.",
    functions=[
        transfer_to_payments_agent,
        transfer_to_policy_agent,
        transfer_to_sales_product_agent,
        transfer_to_warehouse_agent,
        transfer_to_technical_support_agent,
        transfer_to_account_agent,
        transfer_to_feedback_agent,
        transfer_to_appointment_agent,
        transfer_to_billing_agent,
        transfer_to_jira_agent,
        transfer_to_quote_agent
    ]
)

payments_agent = Agent(
    name="Payments Agent",
    instructions="You are an expert on payment options and payment issues. Always respond in English.",
    functions=[
        handle_payments,
        transfer_to_policy_agent,
        transfer_to_sales_product_agent,
        transfer_to_warehouse_agent,
        transfer_to_technical_support_agent,
        transfer_to_account_agent,
        transfer_to_feedback_agent,
        transfer_to_appointment_agent,
        transfer_to_billing_agent,
        transfer_to_jira_agent,
        transfer_to_quote_agent
    ]
)

policy_agent = Agent(
    name="Policy Agent",
    instructions="You provide information about return policies and guarantees. Always respond in English.",
    functions=[
        provide_policy_information,
        transfer_to_payments_agent,
        transfer_to_sales_product_agent,
        transfer_to_warehouse_agent,
        transfer_to_technical_support_agent,
        transfer_to_account_agent,
        transfer_to_feedback_agent,
        transfer_to_appointment_agent,
        transfer_to_billing_agent,
        transfer_to_jira_agent,
        transfer_to_quote_agent
    ]
)

sales_product_agent = Agent(
    name="Sales Product Agent",
    instructions="You provide detailed information about products and services offered by the web agency.Always respond in English.",
    functions=[
        list_products,
        transfer_to_payments_agent,
        transfer_to_policy_agent,
        transfer_to_warehouse_agent,
        transfer_to_technical_support_agent,
        transfer_to_account_agent,
        transfer_to_feedback_agent,
        transfer_to_appointment_agent,
        transfer_to_billing_agent,
        transfer_to_jira_agent,
        transfer_to_quote_agent
    ]
)

warehouse_agent = Agent(
    name="Warehouse Agent",
    instructions="You check the availability of products in the warehouse.Always respond in English.",
    functions=[
        check_warehouse_status,
        transfer_to_payments_agent,
        transfer_to_policy_agent,
        transfer_to_sales_product_agent,
        transfer_to_technical_support_agent,
        transfer_to_account_agent,
        transfer_to_feedback_agent,
        transfer_to_appointment_agent,
        transfer_to_billing_agent,
        transfer_to_jira_agent,
        transfer_to_quote_agent
    ]
)

technical_support_agent = Agent(
    name="Technical Support Agent",
    instructions="You provide technical support for issues with the product.Always respond in English.",
    functions=[
        handle_technical_support,
        transfer_to_payments_agent,
        transfer_to_policy_agent,
        transfer_to_sales_product_agent,
        transfer_to_warehouse_agent,
        transfer_to_account_agent,
        transfer_to_feedback_agent,
        transfer_to_appointment_agent,
        transfer_to_billing_agent,
        transfer_to_jira_agent,
        transfer_to_quote_agent
    ]
)

account_agent = Agent(
    name="Account Agent",
    instructions="You handle issues related to user accounts, such as password resets and account recovery.Always respond in English.",
    functions=[
        handle_account_issues,
        transfer_to_payments_agent,
        transfer_to_policy_agent,
        transfer_to_sales_product_agent,
        transfer_to_warehouse_agent,
        transfer_to_technical_support_agent,
        transfer_to_feedback_agent,
        transfer_to_appointment_agent,
        transfer_to_billing_agent,
        transfer_to_jira_agent,
        transfer_to_quote_agent
    ]
)

feedback_agent = Agent(
    name="Feedback Agent",
    instructions="You collect and process customer feedback to help improve services.Always respond in English.",
    functions=[
        handle_feedback,
        transfer_to_payments_agent,
        transfer_to_policy_agent,
        transfer_to_sales_product_agent,
        transfer_to_warehouse_agent,
        transfer_to_technical_support_agent,
        transfer_to_account_agent,
        transfer_to_appointment_agent,
        transfer_to_billing_agent,
        transfer_to_jira_agent,
        transfer_to_quote_agent
    ]
)

appointment_agent = Agent(
    name="Appointment Agent",
    instructions="You handle appointment bookings for consultations. Always respond in English.",
    functions=[
        handle_appointment_booking,
        transfer_to_payments_agent,
        transfer_to_policy_agent,
        transfer_to_sales_product_agent,
        transfer_to_warehouse_agent,
        transfer_to_technical_support_agent,
        transfer_to_account_agent,
        transfer_to_feedback_agent,
        transfer_to_billing_agent,
        transfer_to_jira_agent,
        transfer_to_quote_agent
    ]
)

billing_agent = Agent(
    name="Billing Agent",
    instructions="You handle customer billing and invoicing queries. Always respond in English.",
    functions=[
        handle_billing_queries,
        transfer_to_payments_agent,
        transfer_to_policy_agent,
        transfer_to_sales_product_agent,
        transfer_to_warehouse_agent,
        transfer_to_technical_support_agent,
        transfer_to_account_agent,
        transfer_to_feedback_agent,
        transfer_to_appointment_agent,
        transfer_to_jira_agent,
        transfer_to_quote_agent
    ]
)

order_creation_agent = Agent(
    name="Order Creation Agent",
    instructions="You assist customers in creating orders, acting as a consultant. Always respond in English.",
    functions=[
        create_order,
        transfer_to_jira_agent,
        transfer_to_quote_agent
    ]
)

jira_agent = Agent(
    name="Jira Task Agent",
    instructions="You create a Jira task (fictitious) to process the customer's order. Always respond in English.",
    functions=[
        create_jira_task,
        transfer_to_payments_agent,
        transfer_to_policy_agent,
        transfer_to_sales_product_agent,
        transfer_to_warehouse_agent,
        transfer_to_technical_support_agent,
        transfer_to_account_agent,
        transfer_to_feedback_agent,
        transfer_to_appointment_agent,
        transfer_to_billing_agent,
        transfer_to_quote_agent
    ]
)

quote_agent = Agent(
    name="Quote Agent",
    instructions="You generate quotes for customers based on the product list and pricing. Always respond in English.",
    functions=[
        create_quote,
        transfer_to_payments_agent,
        transfer_to_policy_agent,
        transfer_to_sales_product_agent,
        transfer_to_warehouse_agent,
        transfer_to_technical_support_agent,
        transfer_to_account_agent,
        transfer_to_feedback_agent,
        transfer_to_appointment_agent,
        transfer_to_billing_agent,
        transfer_to_jira_agent
    ]
)

# Flask web UI
@app.route('/', methods=['GET', 'POST'])
def index():
    # Reimposta la cronologia della chat quando la pagina viene caricata con una richiesta GET (inizio di una nuova sessione)
    if request.method == 'GET' or 'chat_history' not in session:
        session['chat_history'] = [{"role": "agent", "content": "Hello, welcome to our live chat! How can we assist you today?"}]
    
    if request.method == 'POST':
        user_input = request.form.get('user_input')
        if user_input:
            # Aggiungi il messaggio dell'utente alla cronologia
            session['chat_history'].append({"role": "user", "content": user_input})

            # Genera la risposta dell'agente appropriato
            agent_response = client.run(
                agent=customer_care_agent,
                messages=[{"role": "user", "content": user_input}],
            )

            # Imposta l'agente corrente in sessione
            session['current_agent'] = agent_response.agent.name
            
            # Stampa per analizzare la risposta
            print(f"Debug agent_response: {agent_response}")

            # Modifica nel codice di gestione dei messaggi di trasferimento tra agenti
            try:
                response_added = False
                for message in agent_response.messages:
                    # Aggiungi i messaggi di trasferimento tra agenti solo se non già aggiunti
                    if message['role'] == 'tool' and message.get('content'):
                        try:
                            content_dict = json.loads(message['content'])
                            if "assistant" in content_dict:
                                agent_name = content_dict["assistant"]
                                if session.get('current_agent') != agent_name:
                                    transfer_message = f"Transferring you to {agent_name} for further assistance."
                                    session['chat_history'].append({"role": "agent", "content": transfer_message})
                                    session['current_agent'] = agent_name
                        except json.JSONDecodeError:
                            continue

                    # Aggiungi tutte le risposte dell'assistente
                    elif message['role'] == 'assistant' and message.get('content'):
                        session['chat_history'].append({"role": "agent", "content": message['content']})

            except (AttributeError, IndexError, KeyError):
                session['chat_history'].append({"role": "agent", "content": "There was an error retrieving the response. Please try again later."})
                # Salva la cronologia della chat nella sessione
                session.modified = True

    return render_template('index.html', chat_history=session['chat_history'])

if __name__ == "__main__":
    app.run(debug=True, port=5000)