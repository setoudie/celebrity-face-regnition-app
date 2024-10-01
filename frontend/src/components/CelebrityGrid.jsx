import {
  Card,
  CardBody,
  CardFooter,
  Image,
  Stack,
  Heading,
  Text,
  Button,
  ButtonGroup,
  Divider
} from '@chakra-ui/react';
import { useState, useEffect } from 'react';

const CelebrityGrid = () => {
  const [celebrity, setCelebrity] = useState([]); // État pour stocker les données de la célébrité
  const [loading, setLoading] = useState(true);     // État pour le chargement des données

  // Fonction pour récupérer les données depuis l'API
  useEffect(() => {
    const fetchCelebrity = async () => {
      try {
        const response = await fetch('http://127.0.0.1:8000/face/celebrities/'); // Remplace l'URL par ton endpoint API
        const data = await response.json();
        setCelebrity(data);   // Mise à jour de l'état avec les données reçues
        setLoading(false);    // Fin du chargement
        console.log(data);
      } catch (error) {
        console.error('Erreur lors de la récupération des données :', error);
        setLoading(false);
      }
    };

    fetchCelebrity();
  }, []);  // Le tableau vide [] signifie que l'effet s'exécute une seule fois après le premier rendu

  // Affichage d'un message de chargement ou du contenu de la carte
  if (loading) {
    return <Text>Loading...</Text>;
  }

  if (!celebrity) {
    return <Text>Failed to load celebrity data</Text>;
  }

  return (
    <Card maxW='sm'>
      <CardBody>
        <Image
          src={'https://via.placeholder.com/150'} // Image par défaut si imageUrl est null
          alt={celebrity.last_name}
          borderRadius='lg'
        />
        <Stack mt='6' spacing='3'>
          <Heading size='md'>{celebrity.first_name} {celebrity.last_name}</Heading>
          <Text>{celebrity.profession}</Text>
        </Stack>
      </CardBody>
      <Divider />
      <CardFooter>
        <ButtonGroup spacing='2'>
          <Button variant='solid' colorScheme='blue'>
            Follow
          </Button>
          <Button variant='ghost' colorScheme='blue'>
            Share
          </Button>
        </ButtonGroup>
      </CardFooter>
    </Card>
  );
};

export default CelebrityGrid;
