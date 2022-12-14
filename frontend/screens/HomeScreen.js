import { Dimensions, StyleSheet, View } from "react-native";
import React, { useLayoutEffect, useState, useRef } from "react";
import { LineChart } from "react-native-chart-kit";
import { Picker } from "@react-native-picker/picker";
import { Button, Text } from "react-native-elements";

const linedata = {
    labels: ["January", "February", "March", "April", "May", "June", "July"],
    datasets: [
        {
            data: [20, 45, 28, 80, 99, 43, 50],
            strokeWidth: 2, // optional
        },
    ],
};

const HomeScreen = ({ navigation }) => {
    const [selectedDB, setSelectedDB] = useState(0);
    const [chartData, setchartData] = useState(linedata);
    const [currentScale, setCurrentScale] = useState('minute');
const timerRef = useRef(null);

const getData = async () => {
    timerRef.current = setInterval(async () => {
        console.log(currentScale);
        if (currentScale == 'minute') {
            await getTime(currentScale);
        }
    }, 5000);
};

    async function getTime(time) {
        doSomething(time);
        console.log(currentScale, time);
        const endpoint = "https://backend.ambizen.tryhard.fr/data/1/" + time;
        const response = await fetch(endpoint);
        const data = await response.json();
        setchartData({
            labels: data.time,
            datasets: [
                {
                    data: data.decibels,
                    strokeWidth: 2, // optional
                },
            ],
        });
    }

    function doSomething(time) {
        setCurrentScale(time)
    }
/*     setTimeout(async () => {
        console.log(currentScale);
        if (currentScale == 'minute') {
            await getTime(currentScale);
    }
    }, 1000); */

    React.useEffect(() => {
        getData();
        return () => {
            clearInterval(timerRef.current);
        };
    }, []);
    async function getDecibel() {
        const endpoint = "https://backend.ambizen.tryhard.fr/config/1";
        const response = await fetch(endpoint).then((response) =>
            response.json()
        );
        setSelectedDB(response.threshold);
    }

    getDecibel();

    async function sendDecibel(value) {
        const endpoint = "https://backend.ambizen.tryhard.fr/config/1";
        const response = await fetch(endpoint, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                threshold: value,
            }),
        });
        console.log(response);
        if (response.status != 200) {
            alert("Error while sending decibel");
        }
    }

    const decibel = [];
    for (let i = 100; i >= 30; i--) {
        decibel.push(i);
    }

    useLayoutEffect(() => {
        navigation.setOptions({
            headerBackTitle: "Logout",
        });
    }, [navigation]);
    return (
        <View>
            <LineChart
                data={chartData}
                width={Dimensions.get("window").width} // from react-native
                height={220}
                yAxisSuffix={" dB"}
                chartConfig={{
                    backgroundColor: "#93C157",
                    backgroundGradientFrom: "#93C157",
                    backgroundGradientTo: "#52ae6d",
                    decimalPlaces: 2, // optional, defaults to 2dp
                    color: (opacity = 1) => `rgba(255, 255, 255, ${opacity})`,
                    style: {
                        borderRadius: 16,
                    },
                }}
                bezier
                style={{
                    marginVertical: 8,
                    borderRadius: 16,
                }}
            />
            <View style={styles.selections}>
                <Button
                    style={styles.buttons}
                    buttonStyle={{ backgroundColor: "#93C157" }}
                    title="Minute"
                    onPress={() => getTime("minute")}
                />
                <Button
                    style={styles.buttons}
                    buttonStyle={{ backgroundColor: "#93C157" }}
                    title="Hour"
                    onPress={() => getTime("hour")}
                />
                <Button
                    style={styles.buttons}
                    buttonStyle={{ backgroundColor: "#93C157" }}
                    title="Day"
                    onPress={() => getTime("day")}
                />
                <Button
                    style={styles.buttons}
                    buttonStyle={{ backgroundColor: "#93C157" }}
                    title="Week"
                    onPress={() => getTime("week")}
                />
                <Button
                    style={styles.buttons}
                    buttonStyle={{ backgroundColor: "#93C157" }}
                    title="Month"
                    onPress={() => getTime("month")}
                />
            </View>

            <Text h4 style={styles.title}>
                {" "}
                Please select the allowed decibel level{" "}
            </Text>

            <Picker
                selectedValue={selectedDB}
                onValueChange={(itemValue, itemIndex) => {
                    setSelectedDB(itemValue);
                    sendDecibel(itemValue);
                }}
                style={styles.picker}
            >
                {decibel.map((db, i) => (
                    <Picker.Item
                        key={i}
                        label={db.toString() + " dB"}
                        value={db}
                    />
                ))}
            </Picker>
        </View>
    );
};

export default HomeScreen;

const styles = StyleSheet.create({
    selections: {
        flexDirection: "row",
        justifyContent: "space-around",
    },
    buttons: {
        width: 75,
    },
    title: {
        textAlign: "center",
        marginTop: 20,
    },
    picker: {
        height: 50,
        width: 150,
        alignSelf: "center",
        marginTop: 20,
    },
});
