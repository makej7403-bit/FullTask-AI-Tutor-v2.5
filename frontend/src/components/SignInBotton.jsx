import React from "react";
import { auth, provider, signInWithPopup } from "../firebase";

export const SignInButton: React.FC = () => {
  const handleSignIn = async () => {
    try {
      const result = await signInWithPopup(auth, provider);
      const user = result.user;
      console.log("Signed in as:", user?.displayName);
      // Send token to backend if you implement Firebase ID token verification
    } catch (err) {
      console.error("Sign-in error", err);
    }
  };

  return <button onClick={handleSignIn}>Sign in with Google</button>;
};
