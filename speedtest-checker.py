import speedtest

def check_speed():
    print("Initializing speed test...")
    st = speedtest.Speedtest()
        
    print("Finding optimal server...")
    st.get_best_server()
       
    print("Testing download speed...")
    download_speed = st.download() / 1_000_000  # Convert to Mbps
        
    print("Testing upload speed...")
    upload_speed = st.upload() / 1_000_000  # Convert to Mbps
      
    ping = st.results.ping
    
    print("\n--- Speed Test Results ---")
    print(f"Download: {download_speed:.2f} Mbps")
    print(f"Upload: {upload_speed:.2f} Mbps")
    print(f"Ping: {ping:.2f} ms")

if __name__ == "__main__":
    check_speed()
