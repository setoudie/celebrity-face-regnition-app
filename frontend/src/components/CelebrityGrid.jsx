import {
  Flex,
  Text,
} from '@chakra-ui/react';
import { useState, useEffect } from 'react';
import CelebrityCard from './CelebrityCard';  // Assurez-vous que le composant CelebrityCard est bien défini

const CelebrityGrid = () => {
  const [celebrities, setCelebrities] = useState([]); // État pour stocker les données de célébrités
  const [loading, setLoading] = useState(true);       // État pour le chargement des données

  // Fonction pour récupérer les données depuis l'API
  useEffect(() => {
    const fetchCelebrities = async () => {
      try {
        const response = await fetch('http://127.0.0.1:8000/face/celebrities/'); // Remplace l'URL par ton endpoint API
        const data = await response.json();
        setCelebrities(data);   // Mise à jour de l'état avec les données reçues
        setLoading(false);      // Fin du chargement
      } catch (error) {
        console.error('Erreur lors de la récupération des données :', error);
        setLoading(false);
      }
    };

    fetchCelebrities();
  }, []);  // Le tableau vide [] signifie que l'effet s'exécute une seule fois après le premier rendu

  // Affichage d'un message de chargement
  if (loading) {
    return <Text>Loading...</Text>;
  }

  // Affichage d'un message d'erreur si aucune donnée n'est reçue
  if (!celebrities.length) {
    return <Text>Failed to load celebrity data</Text>;
  }

  // Rendu de la grille des célébrités
  return (
    <Flex wrap="wrap" justifyContent="center" gap={6}>
      {celebrities.map((celebrity) => (
        <CelebrityCard
          // key={celebrity.id}  // Ajout de la clé unique pour chaque carte
          name={celebrity.first_name}
          surname={celebrity.last_name}
          imageUrl={celebrity.link}
          profession={celebrity.profession}
        />
      ))}
    </Flex>
  );
};

export default CelebrityGrid;
