import { KeyboardAvoidingView, StyleSheet, Text, View } from "react-native";
import React, { useState } from "react";
import { Button, Input, Image } from "react-native-elements";
import { StatusBar } from "expo-status-bar";

const LoginScreen = ({ navigation }) => {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    async function signIn() {
        const endpoint = "http://localhost:8000/login";
        const response = await fetch(endpoint, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                email: email,
                password: password,
            }),
        });
        console.log(response);
        if (response.status === 200) {
            navigation.navigate("Home");
        } else {
            alert("Invalid credentials");
        }
    }

    return (
        <KeyboardAvoidingView behavior="padding" style={styles.container}>
            <StatusBar style="light" />
            <Image
                source={{
                    uri: "https://i0.wp.com/filecr.com/wp-content/uploads/2021/09/sound-meter-logo.png",
                }}
                style={{ width: 200, height: 200 }}
            />
            <View style={styles.inpuContainer}>
                <Input
                    placeholder="Email"
                    autofocus
                    type="email"
                    value={email}
                    onChangeText={(text) => setEmail(text)}
                />
                <Input
                    placeholder="Password"
                    secureTextEntry
                    type="password"
                    value={password}
                    onChangeText={(text) => setPassword(text)}
                />
            </View>
            <Button
                title={"Login"}
                onPress={signIn}
                containerStyle={styles.button}
                buttonStyle={{ backgroundColor: "#e84e48" }}
            />
            <Button
                title={"Register"}
                type="outline"
                onPress={() => navigation.navigate("Register")}
                containerStyle={styles.button}
                titleStyle={{ color: "#e84e48" }}
                buttonStyle={{ borderColor: "#e84e48" }}
            />
            <View style={{ height: 100 }} />
        </KeyboardAvoidingView>
    );
};

export default LoginScreen;

const styles = StyleSheet.create({
    container: {
        flex: 1,
        alignItems: "center",
        justifyContent: "center",
        padding: 10,
        backgroundColor: "white",
    },
    inpuContainer: {
        width: 300,
    },
    button: {
        width: 200,
        marginTop: 10,
    },
});
