import streamlit

def hello_world():
    return "Hello, world!"

def main():
    streamlit.title("Hello World App")
    streamlit.write(hello_world())
    
if __name__ == "__main__":
    main()