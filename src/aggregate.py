import pandas as pd
import matplotlib.pyplot as plt


def aggregate_total_traffic_per_application(df: pd.DataFrame):
    applications = ['Social Media', 'Google', 'Email', 'Youtube', 'Netflix', 'Gaming', 'Other']
    application_traffic = {}
    
    for app in applications:
        dl_col = f'{app} DL (Bytes)'
        ul_col = f'{app} UL (Bytes)'
        traffic_col = f'{app}_total_traffic'
        
        if dl_col in df.columns and ul_col in df.columns:
            df[traffic_col] = df[dl_col] + df[ul_col]
            application_traffic[app] = df[traffic_col].sum()
        else:
            print(f"Columns {dl_col} or {ul_col} are missing in the DataFrame.")
            application_traffic[app] = None

    print("Aggregate Total Traffic per Application:")
    for app, traffic in application_traffic.items():
        if traffic is not None:
            print(f"{app}: {traffic} Bytes")
        else:
            print(f"{app}: Data missing.")

def top_10_most_engaged_users_per_application(df: pd.DataFrame):
    applications = ['Social Media', 'Google', 'Email', 'Youtube', 'Netflix', 'Gaming', 'Other']
    for app in applications:
        traffic_col = f'Total {app} Traffic'
        df[traffic_col] = df[f'{app} DL (Bytes)'] + df[f'{app} UL (Bytes)']
        app_traffic = df.groupby('MSISDN/Number')[traffic_col].sum()
        top_10_app_users = app_traffic.nlargest(10)
        print(f"Top 10 Most Engaged Users for {app}:")
        print(top_10_app_users)

def identify_top_3_most_used_applications(df: pd.DataFrame):
    applications = ['Social Media', 'Google', 'Email', 'Youtube', 'Netflix', 'Gaming', 'Other']
    application_traffic = {}
    for app in applications:
        dl_col = f'{app} DL (Bytes)'
        ul_col = f'{app} UL (Bytes)'
        traffic_col = f'{app}_total_traffic'
        df[traffic_col] = df[dl_col] + df[ul_col]
        application_traffic[app] = df[traffic_col].sum()

    top_3_apps = sorted(application_traffic.items(), key=lambda x: x[1], reverse=True)[:3]
    print("Top 3 Most Used Applications:")
    for app, traffic in top_3_apps:
        print(f"{app}: {traffic} Bytes")
    return top_3_apps

def plot_top_3_most_used_applications(df: pd.DataFrame):
    top_3_apps = identify_top_3_most_used_applications(df)
    top_3_apps_df = pd.DataFrame(top_3_apps, columns=['Application', 'Total Traffic'])

    plt.figure(figsize=(10, 5))
    plt.bar(top_3_apps_df['Application'], top_3_apps_df['Total Traffic'], color=['blue', 'green', 'red'])
    plt.title('Top 3 Most Used Applications (Total Traffic)')
    plt.ylabel('Total Traffic (Bytes)')
    plt.xticks(rotation=45)
    plt.savefig('../data/top_3_applications.png')
    plt.show()
