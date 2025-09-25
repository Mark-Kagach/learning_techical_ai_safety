export interface UserQuery {
    query: string;
}

export interface SimilarParagraph {
    id: number;
    paragraph: string;
    source: string;
    similarity: number;
}

export interface QueryResponse {
    similarParagraphs: SimilarParagraph[];
}

export type Vector = number[];

// Simple request handler for processing queries
export interface ProcessQueryRequest {
    method: "process_query";
    params: {
        query: string;
    };
}

export interface ProcessQueryResponse {
    response: SimilarParagraph[];
}
