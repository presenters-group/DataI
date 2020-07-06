export interface IDataSource {
  columns : any[],
  columnsVisibility: any[],
  rowsVisibility: any[],
  name : string,
  properties : any,
  rightToLeft : boolean,
  aggregator : any,
  isDeleted : boolean,
  valueCategories: any[]
}
