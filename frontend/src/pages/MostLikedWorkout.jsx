import React from "react";
import axios from 'axios';
import { Button } from "antd";
import { useEffect} from "react";
import { useNavigate } from 'react-router-dom';



const MostLikedWorkout = () => {

    const navigate = useNavigate();

    const redirect_auth= () => {
        navigate('/auth')
    }

    useEffect(() => {
        GetMostLikedWorkout()
      }, []);
    
    
    function GetMostLikedWorkout() {
        axios.get(
            'http://127.0.0.1:80/api/workouts/most_liked',
            { withCredentials: true }
            ).then(
              r =>  {
                console.log(r)
              }
            ).catch((error) => {
                if(error.status == 401){
                    redirect_auth()
                }
              }
            )
        }

    

    
    
    return(
        <div>
            
        </div>
    );

    
};



export default MostLikedWorkout

