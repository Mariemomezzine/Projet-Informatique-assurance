
from flask import Flask, jsonify, Response, request
import pandas as pd
import tradermade as tm
import matplotlib.pyplot as plt
import io 
from flask_cors import CORS
import numpy as np
from datetime import datetime, timedelta

app = Flask(__name__)
CORS(app, resources={r"/get_forex_data": {"origins": "http://localhost:4200"}})
CORS(app, resources={r"/get_historical_data": {"origins": "http://localhost:4200"}})
CORS(app, resources={r"/calculate_percentage_change": {"origins": "http://localhost:4200"}})
CORS(app, resources={r"/calculate_variance": {"origins": "http://localhost:4200"}})
CORS(app, resources={r"/calculate_stdev": {"origins": "http://localhost:4200"}})
CORS(app, resources={r"/calculate_mean": {"origins": "http://localhost:4200"}})
CORS(app, resources={r"/markowitz_plot": {"origins": "http://localhost:4200"}})

tm.set_rest_api_key("w2lpXtLBOw2fSITxmocZ")
@app.route('/get_forex_data', methods=['GET'])
def get_forex_data():
    forex_data = tm.live(currency='EURUSD,GBPUSD,AUDUSD,USDZAR,USDSEK,NZDUSD,USDCAD,USDCHF,USDRUB', fields=["bid", "mid", "ask"])

    # Convert the DataFrame to a list of dictionaries
    forex_data_list = forex_data.to_dict(orient='records')

    return jsonify(forex_data_list)
@app.route('/get_historical_data', methods=['GET'])
def get_historical_data():
    currency_pair = request.args.get('currency')
    start_date = datetime.now().replace(day=1).strftime('%Y-%m-%d')
    end_date = datetime.now().strftime('%Y-%m-%d')
    interval = "daily"
    fields = ["open", "high", "low", "close"]
    data = tm.timeseries(currency=currency_pair, start=start_date, end=end_date, interval=interval, fields=fields)
    data_dict = data.to_dict(orient='records')
    return jsonify(data_dict)

@app.route('/calculate_percentage_change', methods=['GET'])
def calculate_percentage_change():
    currency_pairs = ["EURUSD", "GBPUSD", "AUDUSD", "USDZAR", "USDSEK", "NZDUSD", "USDCAD", "USDCHF", "USDRUB"]
    start_date = "2023-10-23"
    end_date = "2023-10-28"
    interval = "daily"
    fields = ["open", "high", "low", "close"]

    result_dict = {}

    for pair in currency_pairs:
        data = tm.timeseries(currency=pair, start=start_date, end=end_date, interval=interval, fields=fields)

        # Calculate the percentage change for the close prices
        data['percentage_change'] = (data['close'] - data['close'].shift(1)) / data['close'].shift(1)

        # Extract relevant columns and convert to a list of dictionaries
        data_dict = data[['date', 'close', 'percentage_change']].to_dict(orient='records')

        # Store the result for this currency pair in the dictionary
        result_dict[pair] = data_dict

    return jsonify(result_dict)
@app.route('/calculate_mean', methods=['GET'])
def calculate_mean():
    currency_pairs = ["EURUSD", "GBPUSD", "AUDUSD", "USDZAR", "USDSEK", "NZDUSD", "USDCAD", "USDCHF", "USDRUB"]
    start_date = "2023-10-23"
    end_date = "2023-10-27"
    interval = "daily"
    fields = ["open", "high", "low", "close"]

    mean_results = {}

    for pair in currency_pairs:
        data = tm.timeseries(currency=pair, start=start_date, end=end_date, interval=interval, fields=fields)

        # Calculate the percentage change for the close prices
        data['percentage_change'] = (data['close'] - data['close'].shift(1)) / data['close'].shift(1)

        # Calculate the mean (average) of the percentage change
        mean_percentage_change = data['percentage_change'].mean()

        # Store the mean result for this currency pair in the dictionary
        mean_results[pair] = mean_percentage_change

    return jsonify(mean_results)



@app.route('/calculate_variance', methods=['GET'])
def calculate_variance():
    currency_pairs = ["EURUSD", "GBPUSD", "AUDUSD", "USDZAR", "USDSEK", "NZDUSD", "USDCAD", "USDCHF", "USDRUB"]
    start_date = "2023-10-23"
    end_date = "2023-10-28"
    interval = "daily"
    fields = ["open", "high", "low", "close"]

    variance_results = {}

    for pair in currency_pairs:
        data = tm.timeseries(currency=pair, start=start_date, end=end_date, interval=interval, fields=fields)

        # Calculate the percentage change for the close prices
        data['percentage_change'] = (data['close'] - data['close'].shift(1)) / data['close'].shift(1)

        # Calculate the variance of the percentage change
        variance_percentage_change = data['percentage_change'].var()

        # Store the variance result for this currency pair in the dictionary
        variance_results[pair] = variance_percentage_change

    return jsonify(variance_results)

@app.route('/calculate_stdev', methods=['GET'])
def calculate_stdev():
    currency_pairs = ["EURUSD", "GBPUSD", "AUDUSD", "USDZAR", "USDSEK", "NZDUSD", "USDCAD", "USDCHF", "USDRUB"]
    start_date = datetime.now().replace(day=1).strftime('%Y-%m-%d')
    end_date = datetime.now().strftime('%Y-%m-%d')
    interval = "daily"
    fields = ["open", "high", "low", "close"]

    stdev_results = {}

    for pair in currency_pairs:
        data = tm.timeseries(currency=pair, start=start_date, end=end_date, interval=interval, fields=fields)

        # Calculate the percentage change for the close prices
        data['percentage_change'] = (data['close'] - data['close'].shift(1)) / data['close'].shift(1)

        # Calculate the standard deviation (stdev) of the percentage change
        stdev_percentage_change = data['percentage_change'].std()

        # Store the standard deviation result for this currency pair in the dictionary
        stdev_results[pair] = stdev_percentage_change

    return jsonify(stdev_results)

@app.route('/markowitz_plot', methods=['GET'])
def markowitz_plot():
    currency_pairs = ["EURUSD", "GBPUSD", "AUDUSD", "USDZAR", "USDSEK", "NZDUSD", "USDCAD", "USDCHF", "USDRUB"]
    start_date = "2023-10-23"
    end_date = "2023-10-28"
    interval = "daily"
    fields = ["open", "high", "low", "close"]

    mean_list = []
    stdev_list = []
    currency_labels = []

    for pair in currency_pairs:
        data = tm.timeseries(currency=pair, start=start_date, end=end_date, interval=interval, fields=fields)
        data['percentage_change'] = (data['close'] - data['close'].shift(1)) / data['close'].shift(1)
        mean_percentage_change = data['percentage_change'].mean()
        stdev_percentage_change = data['percentage_change'].std()
        mean_list.append(mean_percentage_change)
        stdev_list.append(stdev_percentage_change)
        currency_labels.append(pair)

    # Find the index of the currency with the highest mean and lowest stdev
    max_mean_index = np.argmax(mean_list)
    min_stdev_index = np.argmin(stdev_list)

    # Create a bar chart
    fig, ax = plt.subplots(figsize=(10, 6))
    x = np.arange(len(currency_labels))
    width = 0.35
    bars_mean = ax.bar(x - width/2, mean_list, width, label='Mean')
    bars_stdev = ax.bar(x + width/2, stdev_list, width, label='Standard Deviation')

    # Color the bars for the currency with the highest mean and lowest stdev differently
    bars_mean[max_mean_index].set_color('green')
    bars_stdev[min_stdev_index].set_color('red')

    ax.set_ylabel('Values')
    ax.set_title('Currency Pairs by Mean and Standard Deviation')
    ax.set_xticks(x)
    ax.set_xticklabels(currency_labels)
    ax.legend()

    # Save the plot to a BytesIO object
    img_buffer = io.BytesIO()
    plt.savefig(img_buffer, format='png')
    img_buffer.seek(0)

    # Return the image as a response
    return Response(img_buffer.read(), content_type='image/png')


def executer_strategie_en_temps_reel(market_data):
    # Paramètres de la stratégie (à ajuster en fonction de votre logique spécifique)
    moyenne_mobile_courte = 15
    moyenne_mobile_longue = 50

    # Calculer les moyennes mobiles
    market_data['moyenne_mobile_courte'] = market_data['close'].rolling(window=moyenne_mobile_courte, min_periods=1).mean()
    market_data['moyenne_mobile_longue'] = market_data['close'].rolling(window=moyenne_mobile_longue, min_periods=1).mean()

    # Signaux d'achat et de vente (1 pour achat, -1 pour vente, 0 pour ne rien faire)
    market_data['signal'] = 0
    market_data.loc[market_data['moyenne_mobile_courte'] > market_data['moyenne_mobile_longue'], 'signal'] = 1
    market_data.loc[market_data['moyenne_mobile_courte'] < market_data['moyenne_mobile_longue'], 'signal'] = -1

    # Filtrer les faux signaux (par exemple, éviter les changements de signal trop fréquents)
    market_data['filtered_signal'] = market_data['signal']
    filter_threshold = 0.02  # Adjust as needed
    market_data.loc[
        (market_data['moyenne_mobile_courte'] - market_data['moyenne_mobile_longue']).abs() < filter_threshold,
        'filtered_signal'
    ] = 0

    # Positions (1 pour long, -1 pour short, 0 pour neutre)
    market_data['position'] = market_data['filtered_signal'].diff()

    # Renvoyer les résultats de la stratégie (dernière ligne des données)
    dernier_resultat = market_data.iloc[-6].to_dict()

    return dernier_resultat

@app.route('/get_historic_data', methods=['GET'])
def get_historic_data():
    currency_pair = request.args.get('currency')
    start_date = datetime.now().replace(day=1).strftime('%Y-%m-%d')
    end_date = datetime.now().strftime('%Y-%m-%d')
    interval = "daily"
    fields = ["open", "high", "low", "close"]
    
    # Use tm.timeseries to get historical data
    data = tm.timeseries(currency=currency_pair, start=start_date, end=end_date, interval=interval, fields=fields)

    # Convert the data to a Pandas DataFrame
    data_dict = data.to_dict(orient='records')
    return pd.DataFrame(data_dict)
@app.route('/execute_real_time_strategy', methods=['GET'])
def execute_real_time_strategy():
    currency_pair = request.args.get('currency')

    while True:
        # Obtenez les dernières données du marché
        market_data = get_historic_data()

        # Exécutez la stratégie en temps réel
        resultats_strategie = executer_strategie_en_temps_reel(market_data)

        # Renvoyez les résultats via JSON
        return jsonify(resultats_strategie)

        # Attendez un certain intervalle avant de répéter le processus
        time.sleep(5)


if __name__ == '__main__':
    app.run(debug=True)
