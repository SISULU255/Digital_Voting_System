import streamlit as st

# Define the candidates
candidates = ["Happygod", "Pendo", "Johannes"]

# Define an empty dictionary to store the votes
votes = {}

# Define the main function to render the app
def main():
    st.title("Digital Voting System")

    # Create the user ID input field
    user_id = st.text_input("Enter user ID:")

    # Create the candidate selection dropdown
    candidate = st.selectbox("Select a candidate:", candidates)

    # Create the buttons
    if st.button("Cast Vote"):
        if user_id in votes:
            st.error("You have already voted!")
        else:
            votes[user_id] = candidate
            st.success("Vote cast successfully!")

    if st.button("Destroy Vote"):
        if user_id in votes:
            del votes[user_id]
            st.success("Vote destroyed successfully!")
        else:
            st.error("You have not voted yet.")

    if st.button("Display Results"):
    if len(votes) > 0:
        result_text = "Vote results:\n"
        for candidate in candidates:
            vote_count = list(votes.values()).count(candidate)
            result_text += f"{candidate}: {vote_count}\n"
        st.write(result_text)
    else:
        st.warning("No votes cast yet.")


if __name__ == "__main__":
    main()
