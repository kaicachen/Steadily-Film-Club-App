import { useEffect, useState } from "react";
import { api } from "../services/api";

interface Film {
  id: number;
  film_name: string;
  film_date_discussed: string;
  film_year_released: number;
  film_director: string;
  film_host: number;
}

export default function Home() {
  const [films, setFilms] = useState<Film[]>([]);

  useEffect(() => {
    api.get<Film[]>("/films").then(res => setFilms(res.data));
  }, []);

  return (
    <div className="p-8">
      <h1 className="text-3xl font-bold mb-4">Films</h1>
      <ul>
        {films.map(film => (
          <li key={film.id} className="mb-2 border p-2 rounded">
            <h2 className="font-semibold">{film.film_name} ({film.film_year_released})</h2>
            <p>Director: {film.film_director}</p>
            <p>Date Discussed: {film.film_date_discussed}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}
